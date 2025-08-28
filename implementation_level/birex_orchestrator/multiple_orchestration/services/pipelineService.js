import { coreV1Api, k8sObjectApi } from '../utils/k8sClient.js';
import { sleep } from '../utils/helpers.js';
import * as fs from 'fs';
import * as yaml from 'js-yaml';
import { promisify } from 'util';
import fetch from 'node-fetch';
import { PATH, PROCESSOR_CLOUD, PROCESSOR_EDGE } from '../config/constants.js';

let zone = ['cloud', 'cloud', 'cloud'];

export const isRunning = async (i) => {
  const res = await fetch(`http://birex-processor-${i + 1}:3000/getStatus`);
  return res.json();
};

export const safeDelete = async (i, newZone) => {
  const running = await isRunning(i);
  if (running) {
    try {
      await coreV1Api.deleteNamespacedPod(`processor-${zone[i]}-${i + 1}`, 'default');
      zone[i] = newZone;
    } catch (err) {
      console.error(`Error in delete: ${JSON.stringify(err)}`);
    }
  } else {
    await sleep(3000);
    await safeDelete(i, newZone);
  }
};

export const applySpec = async (i, specPath, newZone) => {
  const specString = await promisify(fs.readFile)(specPath, 'utf8');
  const specs = yaml.loadAll(specString).filter(s => s && s.kind && s.metadata);

  await sleep(500);

  for (const spec of specs) {
    spec.metadata.annotations = {
      ...(spec.metadata.annotations || {}),
      'kubectl.kubernetes.io/last-applied-configuration': JSON.stringify(spec),
    };
    try {
      await k8sObjectApi.read(spec);
      await k8sObjectApi.patch(spec);
    } catch {
      await k8sObjectApi.create(spec);
    }
  }

  await safeDelete(i, newZone);
};

export const moveToEdge = (i) => applySpec(i, `${PATH}${i + 1}${PROCESSOR_EDGE}`, 'edge');
export const moveToCloud = (i) => applySpec(i, `${PATH}${i + 1}${PROCESSOR_CLOUD}`, 'cloud');
export const resetStats = (i) => fetch(`http://birex-processor-${i + 1}:3000/resetStats`);
export const retrieveStats = (i) => fetch(`http://birex-processor-${i + 1}:3000/getStats`).then(res => res.json());
export const getZone = () => zone;
export const setZone = (z) => zone = z;
