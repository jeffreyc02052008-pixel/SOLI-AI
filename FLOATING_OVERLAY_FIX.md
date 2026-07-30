# Floating overlay installation

The panel in your screenshot is Grabix Pro. SOLI AI is a separate extension, so both can appear at the same time.

## Clean installation

1. Open `chrome://extensions`.
2. Remove every older extension named **SOLI AI**, **SOLI AI Overlay**, or **SOLI AI Axiom Overlay**. Keep Grabix only if you still want it.
3. Enable **Developer mode**.
4. Click **Load unpacked**.
5. Select this package's exact `extension` folder—the folder containing `manifest.json`.
6. Open an `https://axiom.trade/...` page and press `Ctrl+Shift+R`.
7. Click the SOLI AI toolbar icon.
8. Press **Force inject + show floating panel**.
9. Close the toolbar popup. The panel appears near the top-center of Axiom.

## Dragging

Hold the empty middle area of the top bar where it says **SOLI AI**, then move the mouse. Do not start the drag on the collapse or menu buttons. Position is saved automatically.

## Recovery

- Press **Reset position** in the toolbar popup.
- When the full panel is hidden, a small `S SOLI AI` launcher pill remains visible.
- Ensure `Lock panel position` is off in Settings.
- If modules say the backend is unavailable, run `python server.py`; the panel itself should still remain visible.
