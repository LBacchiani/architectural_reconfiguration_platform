import express from 'express';
import { sleep } from './utils/helpers.js';
import { setSizes } from './services/sizeManager.js';
import { evaluateMetrics } from './services/loadBalancer.js';
import { resetStats } from './services/pipelineService.js';
import { PORT, HOST } from './config/constants.js';

const app = express();

const monitoring = async () => {
  await sleep(10000);
  for (let i = 0; i < 16; i++) {
    await Promise.all([0, 1, 2].map(resetStats));
    if (i % 2 === 0) await setSizes();
    await sleep(10000);
    await evaluateMetrics();
  }
  console.log('Monitoring complete.');
};

monitoring();
app.listen(PORT, HOST);