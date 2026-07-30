# SOLI AI v3.2

## Floating overlay repair

- Removed the Shadow DOM `<link rel="stylesheet">` dependency.
- Bundled overlay CSS into `overlay_styles.js` and applied it with `adoptedStyleSheets`.
- Removed inert hosts left by older extension reloads.
- Added immediate visible loading and fatal-error fallbacks.
- Added a one-second mount watchdog.
- Added panel diagnostics: version, mounted state, CSS state, visibility, coordinates, width and height.
- Preserved draggable pointer-capture behavior and saved position.

## PumpSwap via pump.fun

- Added PumpSwap filter to the website and overlay Token Finder.
- Labels PumpSwap events as `PumpSwap via pump.fun`.
- Labels pre-migration events as `pump.fun bonding curve`.
- Processes PumpSwap trade events before migration detection.
- Adds `pumpswap` and `migrated` categories to graduated-token events.
- Links Pump/PumpSwap tokens back to `https://pump.fun/coin/<mint>`.

Trading remains paper-only.
