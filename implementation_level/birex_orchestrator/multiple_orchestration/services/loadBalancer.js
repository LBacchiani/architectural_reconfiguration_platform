import { retrieveStats, moveToEdge, moveToCloud, getZone } from './pipelineService.js';
import { logger } from '../utils/logger.js';

export const evaluateMetrics = async () => {
  const stats = await Promise.all([0, 1, 2].map(retrieveStats));
  const latencies = stats.map(s => s.avgLatency);
  const sizes = stats.map(s => s.avgDataSize);
  const zone = getZone();

  logger(zone, stats);

  const maxLatency = Math.max(...latencies);
  const idx = latencies.indexOf(maxLatency);

  if (maxLatency > 1800) {
    if (!zone.includes('edge')) moveToEdge(idx);
    else {
      const edgeIdx = zone.indexOf('edge');
      if (edgeIdx !== idx) {
        moveToCloud(edgeIdx);
        moveToEdge(idx);
      }
    }
  } else if (zone[idx] === 'edge' && maxLatency < 1000 && sizes[idx] < 65 * 65 * 3500) {
    moveToCloud(idx);
  }
};