export type ChairReading = { percent: number; tokens: number; window: number };

declare module "claude-code" {
  interface PluginState {
    "chair": { reading: ChairReading };
  }
}
