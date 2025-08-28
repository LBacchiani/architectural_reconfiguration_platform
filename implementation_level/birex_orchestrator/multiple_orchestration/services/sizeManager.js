import fetch from 'node-fetch';
import { MULTI_SIZES } from '../config/constants.js';

let index = 0;

export const setSizes = async () => {
  await Promise.all([0, 1, 2].map(i => {
    const size = MULTI_SIZES[i][index % MULTI_SIZES[i].length];
    return fetch(`http://birex-collector-${i + 1}:8080/birexcollector/actions/setSizes`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ minSize: size, maxSize: size }),
    }).catch(err => console.error('SetSizes failed', err));
  }));
  index++;
};