#!/usr/bin/env python3
"""
SOLI AI FRONTEND + AXIOM OVERLAY GENERATOR
==========================================

Place this file in the root of your existing SOLI AI project, beside server.py,
then run:

    python build_soli_ai.py --apply

It creates:

    web_static/
        index.html          Public landing page
        dashboard.html      Live memecoin dashboard
        setup.html          Extension setup instructions
        styles.css          Shared website styling
        site.js             Landing/setup interactions
        dashboard.js        Dashboard API integration

    extension/
        manifest.json       Chrome/Edge/Brave extension manifest
        background.js       Local SOLI AI API relay
        content.js          Draggable Axiom overlay
        overlay.css         Overlay styling
        popup.html          Extension popup
        popup.js            Enable/disable controls
        README.md           Extension instructions

The generator backs up an existing web_static or extension directory before
replacing it. It does NOT create live-wallet trading or request private keys.
The generated interface uses the paper-trading endpoints already present in
server.py.
"""

from __future__ import annotations

import argparse
import json
import shutil
from datetime import datetime
from pathlib import Path
from textwrap import dedent

ROOT = Path(__file__).resolve().parent


def clean(text: str) -> str:
    return dedent(text).lstrip("\n")


FILES: dict[str, str] = {
    "web_static/index.html": clean(r'''
        <!doctype html>
        <html lang="en">
        <head>
          <meta charset="utf-8">
          <meta name="viewport" content="width=device-width, initial-scale=1">
          <meta name="description" content="SOLI AI combines live Solana memecoin discovery, risk context, and paper trading.">
          <title>SOLI AI — Memecoin Intelligence</title>
          <link rel="stylesheet" href="/styles.css">
        </head>
        <body>
          <header class="site-nav">
            <a class="brand" href="/">
              <span class="brand-mark">S</span>
              <span>SOLI AI</span>
            </a>
            <nav class="nav-links" aria-label="Primary navigation">
              <a href="#features">Features</a>
              <a href="#advantage">Advantage</a>
              <a href="#workflow">How it works</a>
              <a href="/setup.html">Setup</a>
            </nav>
            <div class="nav-actions">
              <a class="button button-ghost" href="/dashboard.html">Dashboard</a>
              <a class="button button-primary" href="/setup.html">Activate overlay</a>
            </div>
          </header>

          <main>
            <section class="hero section-shell">
              <div class="eyebrow">SOLANA MEMECOIN INTELLIGENCE</div>
              <h1>Trade with context.<br><span>Not guesswork.</span></h1>
              <p class="hero-copy">
                SOLI AI brings live token discovery, market activity, rug-risk context,
                token analysis, watchlists, and paper trading into one streamlined workflow.
              </p>
              <div class="hero-actions">
                <a class="button button-primary button-large" href="/dashboard.html">Launch SOLI AI</a>
                <a class="button button-ghost button-large" href="#features">Explore features</a>
              </div>
              <p class="safety-note">Research and paper-trading software. No token can be proven safe.</p>

              <div class="product-demo" aria-label="SOLI AI product preview">
                <div class="demo-toolbar">
                  <span class="demo-dot"></span><span class="demo-dot"></span><span class="demo-dot"></span>
                  <div class="demo-url">axiom.trade — SOLI AI active</div>
                </div>
                <div class="demo-body">
                  <div class="demo-feed">
                    <div class="demo-column-title">New pairs</div>
                    <article class="demo-token">
                      <div class="token-avatar">M</div>
                      <div><strong>MOONCAT</strong><span>Age 18m · Liquidity $84K</span></div>
                      <b class="positive">+31%</b>
                    </article>
                    <article class="demo-token">
                      <div class="token-avatar">S</div>
                      <div><strong>SOLPUP</strong><span>Age 42m · Liquidity $126K</span></div>
                      <b class="negative">-7%</b>
                    </article>
                    <article class="demo-token">
                      <div class="token-avatar">G</div>
                      <div><strong>GRIT</strong><span>Age 2h · Liquidity $210K</span></div>
                      <b class="positive">+12%</b>
                    </article>
                  </div>
                  <aside class="demo-overlay">
                    <div class="overlay-brand">SOLI AI</div>
                    <h3>Token analysis</h3>
                    <div class="demo-score-row">
                      <div><span>Observed risk</span><strong>38 / 100</strong></div>
                      <span class="risk-chip medium">Medium</span>
                    </div>
                    <div class="mini-grid">
                      <div><span>Liquidity</span><strong>$84K</strong></div>
                      <div><span>Age</span><strong>18m</strong></div>
                      <div><span>1h</span><strong class="positive">+31%</strong></div>
                      <div><span>Buys/Sells</span><strong>442/301</strong></div>
                    </div>
                    <ul class="signal-list">
                      <li class="good">Mint authority appears revoked</li>
                      <li class="warn">Top-holder concentration needs review</li>
                      <li class="warn">Fast price acceleration</li>
                    </ul>
                    <button type="button" class="button button-primary full">Open full analysis</button>
                  </aside>
                </div>
              </div>
            </section>

            <section id="features" class="section-shell content-section">
              <div class="section-heading">
                <div class="eyebrow">ONE CONNECTED WORKFLOW</div>
                <h2>Everything needed to research before acting</h2>
                <p>Use the standalone dashboard for deep research and the Axiom overlay for fast context while browsing tokens.</p>
              </div>
              <div class="feature-grid">
                <article class="feature-card"><div class="feature-icon">AI</div><h3>Live token intelligence</h3><p>Review price, liquidity, market cap, pair age, volume, momentum, and transaction activity.</p></article>
                <article class="feature-card"><div class="feature-icon">R</div><h3>Rug-risk context</h3><p>Inspect authorities, holder concentration, liquidity conditions, token age, and suspicious activity.</p></article>
                <article class="feature-card"><div class="feature-icon">F</div><h3>Token discovery</h3><p>Filter new, trending, and boosted Solana tokens by liquidity, age, volume, momentum, and risk.</p></article>
                <article class="feature-card"><div class="feature-icon">O</div><h3>Axiom overlay</h3><p>Open SOLI AI directly on Axiom with a draggable, resizable, collapsible research panel.</p></article>
                <article class="feature-card"><div class="feature-icon">P</div><h3>Paper trading</h3><p>Practice entries, exits, and position sizing without exposing a wallet or risking real funds.</p></article>
                <article class="feature-card"><div class="feature-icon">W</div><h3>Watchlists and portfolio</h3><p>Track selected tokens, simulated positions, entries, exits, and recent paper-trade activity.</p></article>
              </div>
            </section>

            <section id="advantage" class="section-shell content-section">
              <div class="section-heading">
                <div class="eyebrow">THE SOLI AI ADVANTAGE</div>
                <h2>Make raw data easier to understand</h2>
              </div>
              <div class="advantage-grid">
                <article><span>01</span><h3>Analyze faster</h3><p>Turn a token mint into a readable market and risk summary in seconds.</p></article>
                <article><span>02</span><h3>See the reasons</h3><p>Every rating is paired with visible evidence instead of an unexplained label.</p></article>
                <article><span>03</span><h3>Stay in one workflow</h3><p>Move from discovery to analysis, watchlists, and paper trading without switching tools.</p></article>
                <article><span>04</span><h3>Separate risk from hype</h3><p>View contract, holder, liquidity, momentum, and social signals as different categories.</p></article>
                <article><span>05</span><h3>Practice first</h3><p>Test a plan in paper mode before considering any wallet transaction.</p></article>
                <article><span>06</span><h3>Keep control</h3><p>The local development version does not request private keys or execute live trades.</p></article>
              </div>
            </section>

            <section id="workflow" class="section-shell content-section workflow-section">
              <div class="section-heading">
                <div class="eyebrow">HOW IT WORKS</div>
                <h2>Research a token in four steps</h2>
              </div>
              <div class="workflow-grid">
                <article><div class="step-number">1</div><h3>Start SOLI AI</h3><p>Open the dashboard or activate the browser overlay on Axiom.</p></article>
                <article><div class="step-number">2</div><h3>Select a token</h3><p>Choose an Axiom token or paste a Solana mint manually.</p></article>
                <article><div class="step-number">3</div><h3>Review evidence</h3><p>Inspect liquidity, activity, authorities, holder concentration, and risk flags.</p></article>
                <article><div class="step-number">4</div><h3>Create a plan</h3><p>Watch the token or test an entry using the paper-trading portfolio.</p></article>
              </div>
            </section>

            <section class="section-shell final-cta">
              <div>
                <div class="eyebrow">BUILD SAFELY</div>
                <h2>Start with live research and paper trading</h2>
                <p>Install the local overlay, connect it to your existing SOLI AI backend, and verify every data field before adding wallet execution.</p>
              </div>
              <div class="hero-actions">
                <a class="button button-primary button-large" href="/setup.html">View setup guide</a>
                <a class="button button-ghost button-large" href="/dashboard.html">Open dashboard</a>
              </div>
            </section>
          </main>

          <footer class="site-footer section-shell">
            <a class="brand" href="/"><span class="brand-mark">S</span><span>SOLI AI</span></a>
            <p>Research and paper-trading software. Not financial advice.</p>
            <div><a href="/dashboard.html">Dashboard</a><a href="/setup.html">Setup</a></div>
          </footer>
          <script src="/site.js"></script>
        </body>
        </html>
    '''),
    "web_static/dashboard.html": clean(r'''
        <!doctype html>
        <html lang="en">
        <head>
          <meta charset="utf-8">
          <meta name="viewport" content="width=device-width, initial-scale=1">
          <title>SOLI AI Dashboard</title>
          <link rel="stylesheet" href="/styles.css">
        </head>
        <body class="app-body">
          <header class="site-nav app-nav">
            <a class="brand" href="/"><span class="brand-mark">S</span><span>SOLI AI</span></a>
            <div class="dashboard-search">
              <label class="sr-only" for="global-mint">Token name, ticker, or mint</label>
              <input id="global-mint" type="text" placeholder="Paste a Solana mint">
              <button id="analyze-mint" class="button button-primary" type="button">Analyze</button>
            </div>
            <div class="nav-actions"><a class="button button-ghost" href="/setup.html">Install overlay</a></div>
          </header>

          <div class="app-layout">
            <aside class="app-sidebar">
              <nav>
                <button class="sidebar-link active" data-view="discover">Discover</button>
                <button class="sidebar-link" data-view="analysis">Token analysis</button>
                <button class="sidebar-link" data-view="risk">Rug detector</button>
                <button class="sidebar-link" data-view="watchlist">Watchlist</button>
                <button class="sidebar-link" data-view="portfolio">Paper portfolio</button>
              </nav>
              <div class="sidebar-footer">
                <span class="status-dot"></span>
                <span id="backend-status">Checking backend…</span>
              </div>
            </aside>

            <main class="dashboard-main">
              <section class="dashboard-heading">
                <div><div class="eyebrow">LIVE SOLANA RESEARCH</div><h1>Memecoin intelligence dashboard</h1><p>Discover tokens, inspect risk evidence, and test paper-trading plans.</p></div>
                <button id="refresh-feed" class="button button-primary" type="button">Refresh feed</button>
              </section>

              <section class="metric-row" aria-label="Dashboard metrics">
                <article><span>Tokens shown</span><strong id="metric-tokens">0</strong></article>
                <article><span>Lower observed risk</span><strong id="metric-lower-risk">0</strong></article>
                <article><span>Watchlist</span><strong id="metric-watchlist">0</strong></article>
                <article><span>Last update</span><strong id="metric-update">—</strong></article>
              </section>

              <section class="dashboard-grid">
                <div class="feed-panel">
                  <div class="panel-heading">
                    <div><h2>Live token feed</h2><p id="feed-message">Waiting for backend data…</p></div>
                    <span class="live-badge">LIVE</span>
                  </div>
                  <div class="filter-grid">
                    <label>Search<input id="feed-search" type="search" placeholder="Name, ticker, or mint"></label>
                    <label>Minimum liquidity<input id="min-liquidity" type="number" min="0" step="1000" value="25000"></label>
                    <label>Minimum age (minutes)<input id="min-age" type="number" min="0" value="10"></label>
                    <label>Sort by<select id="sort-by"><option value="liquidity">Liquidity</option><option value="volume">24h volume</option><option value="change">24h change</option><option value="risk">Risk</option></select></label>
                  </div>
                  <div class="feed-tabs" role="tablist">
                    <button class="feed-tab active" data-tab="new" type="button">New</button>
                    <button class="feed-tab" data-tab="trending" type="button">Trending</button>
                    <button class="feed-tab" data-tab="boosted" type="button">Boosted</button>
                    <button class="feed-tab" data-tab="watchlist" type="button">Watchlist</button>
                  </div>
                  <div id="token-list" class="token-list" aria-live="polite"></div>
                </div>

                <aside class="analysis-drawer">
                  <div class="panel-heading"><div><h2>Token analysis</h2><p id="analysis-subtitle">Select a token from the feed.</p></div></div>
                  <div id="analysis-empty" class="empty-state"><div class="empty-icon">S</div><h3>Ready to analyze</h3><p>Select a token or paste a mint above.</p></div>
                  <div id="analysis-content" class="analysis-content hidden">
                    <div class="analysis-token-heading"><div><h3 id="analysis-name">Unknown token</h3><p id="analysis-symbol">—</p></div><span id="analysis-risk-chip" class="risk-chip unknown">Unknown</span></div>
                    <p id="analysis-mint" class="mint-text"></p>
                    <div class="analysis-metrics">
                      <article><span>Price</span><strong id="analysis-price">—</strong></article>
                      <article><span>Liquidity</span><strong id="analysis-liquidity">—</strong></article>
                      <article><span>Volume</span><strong id="analysis-volume">—</strong></article>
                      <article><span>Signal</span><strong id="analysis-signal">—</strong></article>
                    </div>
                    <div class="risk-score-block"><span>Observed risk score</span><strong id="analysis-risk-score">—</strong><div class="risk-track"><span id="analysis-risk-bar"></span></div></div>
                    <div class="analysis-summary"><h3>SOLI AI summary</h3><p id="analysis-summary-text">—</p></div>
                    <div id="analysis-flags" class="flag-list"></div>
                    <div class="analysis-actions">
                      <button id="watch-token" class="button button-ghost" type="button">Add to watchlist</button>
                      <button id="paper-buy-token" class="button button-primary" type="button">Paper buy</button>
                    </div>
                  </div>
                </aside>
              </section>
            </main>
          </div>

          <dialog id="paper-dialog" class="paper-dialog">
            <form method="dialog">
              <button class="dialog-close" value="cancel" aria-label="Close">×</button>
              <div class="eyebrow">PAPER TRADING ONLY</div>
              <h2>Simulate a token purchase</h2>
              <p id="paper-token-label">No token selected.</p>
              <label>Token units<input id="paper-units" type="number" min="0.000001" step="any" value="1"></label>
              <div id="paper-feedback" class="dialog-feedback" aria-live="polite"></div>
              <div class="dialog-actions"><button class="button button-ghost" value="cancel">Cancel</button><button id="confirm-paper-buy" class="button button-primary" type="button">Confirm paper buy</button></div>
            </form>
          </dialog>

          <script src="/dashboard.js"></script>
        </body>
        </html>
    '''),
    "web_static/setup.html": clean(r'''
        <!doctype html>
        <html lang="en">
        <head>
          <meta charset="utf-8">
          <meta name="viewport" content="width=device-width, initial-scale=1">
          <title>Install SOLI AI Overlay</title>
          <link rel="stylesheet" href="/styles.css">
        </head>
        <body>
          <header class="site-nav">
            <a class="brand" href="/"><span class="brand-mark">S</span><span>SOLI AI</span></a>
            <nav class="nav-links"><a href="/">Home</a><a href="/dashboard.html">Dashboard</a></nav>
          </header>
          <main class="section-shell setup-page">
            <div class="section-heading setup-heading">
              <div class="eyebrow">LOCAL DEVELOPMENT SETUP</div>
              <h1>Install the SOLI AI Axiom overlay</h1>
              <p>The development extension communicates only with your local SOLI AI server and does not request wallet keys.</p>
            </div>
            <div class="setup-status"><span class="status-dot"></span><span id="setup-backend-status">Checking http://127.0.0.1:5500…</span></div>
            <section class="setup-grid">
              <article><div class="step-number">1</div><h2>Start the backend</h2><p>Open PowerShell in your project folder and run:</p><pre><code>python server.py</code></pre><p>Keep this terminal open while using the dashboard or overlay.</p></article>
              <article><div class="step-number">2</div><h2>Open extensions</h2><p>In Chrome, Edge, or Brave, open the extensions manager:</p><pre><code>chrome://extensions</code></pre><p>Turn on <strong>Developer mode</strong>.</p></article>
              <article><div class="step-number">3</div><h2>Load the extension</h2><p>Choose <strong>Load unpacked</strong> and select:</p><pre><code>YOUR_PROJECT\extension</code></pre><p>The SOLI AI extension should appear in the extension list.</p></article>
              <article><div class="step-number">4</div><h2>Open Axiom</h2><p>Navigate to Axiom and open a token page. The SOLI AI panel will appear automatically.</p><pre><code>https://axiom.trade/</code></pre><p>Use the extension popup to hide or restore the panel.</p></article>
            </section>
            <section class="troubleshooting">
              <h2>Testing checklist</h2>
              <ol>
                <li>Open <code>http://127.0.0.1:5500/api/status</code> and confirm JSON appears.</li>
                <li>Open <code>http://127.0.0.1:5500/dashboard.html</code> and refresh the feed.</li>
                <li>Load the unpacked extension and refresh Axiom.</li>
                <li>Paste a known Solana mint into the overlay if automatic detection does not find one.</li>
                <li>Keep all trading in paper mode until risk scores and pair data are consistent.</li>
              </ol>
              <div class="warning-box"><strong>Important:</strong> Never place a private key in website JavaScript, extension storage, GitHub, or screenshots. Live trading requires a separate audited backend design.</div>
            </section>
          </main>
          <script src="/site.js"></script>
        </body>
        </html>
    '''),
    "web_static/styles.css": clean(r'''
        :root {
          --bg: #070b16;
          --bg-soft: #0a1020;
          --panel: #0d1424;
          --panel-2: #121b2f;
          --panel-3: #17223a;
          --border: #263657;
          --border-soft: rgba(92, 124, 250, 0.18);
          --text: #f5f7ff;
          --muted: #93a4c7;
          --blue: #5c7cfa;
          --blue-2: #7189ff;
          --cyan: #54c8e8;
          --green: #59d39b;
          --amber: #f3c969;
          --red: #ef7f8f;
          --shadow: 0 24px 70px rgba(0, 0, 0, 0.35);
        }
        * { box-sizing: border-box; }
        html { scroll-behavior: smooth; }
        body { margin: 0; min-width: 320px; background: radial-gradient(circle at 50% -20%, rgba(92,124,250,.14), transparent 35%), var(--bg); color: var(--text); font-family: Inter, ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif; }
        a { color: inherit; text-decoration: none; }
        button, input, select { font: inherit; }
        button { cursor: pointer; }
        .hidden { display: none !important; }
        .sr-only { position: absolute; width: 1px; height: 1px; overflow: hidden; clip: rect(0,0,0,0); white-space: nowrap; }
        .section-shell { width: min(1180px, calc(100% - 40px)); margin: 0 auto; }
        .site-nav { position: sticky; top: 0; z-index: 30; height: 76px; display: flex; align-items: center; gap: 36px; padding: 0 max(24px, calc((100vw - 1180px)/2)); background: rgba(7,11,22,.88); border-bottom: 1px solid rgba(147,164,199,.12); backdrop-filter: blur(18px); }
        .brand { display: inline-flex; align-items: center; gap: 10px; font-weight: 800; letter-spacing: .08em; }
        .brand-mark { display: grid; place-items: center; width: 34px; height: 34px; border-radius: 10px; background: linear-gradient(135deg, var(--blue), var(--cyan)); color: white; box-shadow: 0 10px 30px rgba(92,124,250,.28); }
        .nav-links { display: flex; align-items: center; gap: 28px; color: var(--muted); font-size: 14px; }
        .nav-links a:hover { color: var(--text); }
        .nav-actions { margin-left: auto; display: flex; align-items: center; gap: 10px; }
        .button { display: inline-flex; justify-content: center; align-items: center; min-height: 42px; padding: 0 18px; border-radius: 12px; border: 1px solid transparent; font-weight: 700; color: var(--text); transition: transform .18s ease, border-color .18s ease, background .18s ease; }
        .button:hover { transform: translateY(-1px); }
        .button-primary { background: linear-gradient(135deg, var(--blue), #6967ef 62%, var(--cyan)); color: white; box-shadow: 0 14px 35px rgba(92,124,250,.24); }
        .button-ghost { background: rgba(18,27,47,.72); border-color: var(--border); }
        .button-large { min-height: 54px; padding-inline: 28px; }
        .full { width: 100%; }
        .eyebrow { color: var(--cyan); font-size: 12px; letter-spacing: .18em; font-weight: 800; }
        .hero { padding: 106px 0 72px; text-align: center; }
        .hero h1 { margin: 18px 0 22px; font-size: clamp(52px, 7vw, 92px); line-height: .98; letter-spacing: -.055em; }
        .hero h1 span { background: linear-gradient(90deg, var(--blue), var(--cyan)); -webkit-background-clip: text; background-clip: text; color: transparent; }
        .hero-copy { width: min(760px, 100%); margin: 0 auto; color: var(--muted); font-size: 18px; line-height: 1.7; }
        .hero-actions { display: flex; justify-content: center; gap: 14px; margin-top: 32px; flex-wrap: wrap; }
        .safety-note { color: var(--muted); font-size: 13px; margin-top: 18px; }
        .product-demo { margin-top: 68px; text-align: left; border: 1px solid var(--border); border-radius: 24px; overflow: hidden; background: #080c16; box-shadow: var(--shadow); }
        .demo-toolbar { display: flex; align-items: center; gap: 8px; height: 48px; padding: 0 18px; background: #101728; border-bottom: 1px solid var(--border); }
        .demo-dot { width: 10px; height: 10px; border-radius: 50%; background: #34415f; }
        .demo-url { margin: 0 auto; width: min(360px, 70%); padding: 6px 14px; border-radius: 8px; background: #080d19; color: var(--muted); text-align: center; font-size: 12px; }
        .demo-body { min-height: 490px; display: grid; grid-template-columns: 1fr 390px; gap: 22px; padding: 28px; background: radial-gradient(circle at 72% 15%, rgba(92,124,250,.09), transparent 30%); }
        .demo-feed { border: 1px solid #1b2740; border-radius: 16px; overflow: hidden; background: rgba(10,15,27,.8); }
        .demo-column-title { padding: 16px 18px; font-weight: 800; border-bottom: 1px solid #1b2740; }
        .demo-token { display: grid; grid-template-columns: 48px 1fr auto; align-items: center; gap: 14px; padding: 18px; border-bottom: 1px solid #172139; }
        .demo-token div:nth-child(2) { display: grid; gap: 5px; }
        .demo-token span { color: var(--muted); font-size: 13px; }
        .token-avatar { display: grid; place-items: center; width: 48px; height: 48px; border-radius: 12px; background: linear-gradient(135deg, #25365d, #182139); border: 1px solid #3b4f7e; font-weight: 900; }
        .positive { color: var(--green); }
        .negative { color: var(--red); }
        .demo-overlay { align-self: center; padding: 22px; border-radius: 18px; background: #101622; border: 1px solid #38507f; box-shadow: 0 20px 70px rgba(0,0,0,.45); }
        .overlay-brand { padding-bottom: 14px; text-align: center; color: var(--blue-2); border-bottom: 1px solid #24314e; font-size: 13px; font-weight: 800; letter-spacing: .08em; }
        .demo-score-row { display: flex; align-items: center; justify-content: space-between; margin: 18px 0; }
        .demo-score-row div { display: grid; gap: 6px; }
        .demo-score-row span, .mini-grid span { color: var(--muted); font-size: 12px; }
        .risk-chip { display: inline-flex; align-items: center; justify-content: center; padding: 7px 10px; border-radius: 999px; font-size: 12px; font-weight: 800; }
        .risk-chip.lower { color: #bdf5d7; background: rgba(89,211,155,.16); }
        .risk-chip.medium { color: #ffe9aa; background: rgba(243,201,105,.15); }
        .risk-chip.high, .risk-chip.extreme { color: #ffd0d6; background: rgba(239,127,143,.17); }
        .risk-chip.unknown { color: #d4dcf5; background: rgba(147,164,199,.14); }
        .mini-grid { display: grid; grid-template-columns: repeat(2, 1fr); gap: 10px; }
        .mini-grid div { display: grid; gap: 5px; padding: 12px; border-radius: 12px; background: #151f34; border: 1px solid #23304e; }
        .signal-list { display: grid; gap: 9px; padding: 0; margin: 18px 0; list-style: none; font-size: 13px; }
        .signal-list li::before { content: "•"; margin-right: 8px; }
        .signal-list .good { color: #bdf5d7; }
        .signal-list .warn { color: #ffe4a1; }
        .content-section { padding: 92px 0; }
        .section-heading { width: min(760px, 100%); margin: 0 auto 46px; text-align: center; }
        .section-heading h2, .final-cta h2, .setup-heading h1 { margin: 12px 0 14px; font-size: clamp(34px, 4vw, 54px); letter-spacing: -.04em; }
        .section-heading p, .final-cta p { color: var(--muted); line-height: 1.7; }
        .feature-grid, .advantage-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 20px; }
        .feature-card, .advantage-grid article { min-height: 250px; padding: 28px; background: linear-gradient(180deg, rgba(23,34,58,.92), rgba(14,21,37,.95)); border: 1px solid var(--border); border-radius: 18px; }
        .feature-icon { display: grid; place-items: center; width: 44px; height: 44px; border-radius: 12px; color: #bcd0ff; background: rgba(92,124,250,.12); border: 1px solid rgba(92,124,250,.3); font-weight: 900; }
        .feature-card h3, .advantage-grid h3 { margin: 22px 0 12px; }
        .feature-card p, .advantage-grid p, .workflow-grid p { color: var(--muted); line-height: 1.65; }
        .advantage-grid article > span { color: var(--cyan); font-weight: 900; letter-spacing: .12em; }
        .workflow-section { border-top: 1px solid rgba(147,164,199,.08); }
        .workflow-grid { display: grid; grid-template-columns: repeat(4, 1fr); gap: 20px; }
        .workflow-grid article { text-align: center; padding: 18px; }
        .step-number { display: grid; place-items: center; width: 52px; height: 52px; margin: 0 auto 18px; border-radius: 14px; background: linear-gradient(135deg, var(--blue), #6967ef); font-weight: 900; box-shadow: 0 12px 30px rgba(92,124,250,.22); }
        .final-cta { margin-top: 36px; margin-bottom: 80px; display: flex; justify-content: space-between; align-items: center; gap: 36px; padding: 52px; border: 1px solid var(--border); border-radius: 24px; background: linear-gradient(135deg, rgba(92,124,250,.12), rgba(84,200,232,.05)); }
        .final-cta > div:first-child { max-width: 680px; }
        .site-footer { min-height: 130px; display: flex; align-items: center; gap: 28px; border-top: 1px solid rgba(147,164,199,.1); color: var(--muted); }
        .site-footer p { margin-right: auto; }
        .site-footer div { display: flex; gap: 20px; }
        .setup-page { padding: 80px 0; }
        .setup-heading { text-align: center; width: min(780px, 100%); margin: 0 auto 32px; }
        .setup-heading p { color: var(--muted); line-height: 1.7; }
        .setup-status { width: fit-content; margin: 0 auto 40px; display: flex; align-items: center; gap: 10px; padding: 10px 14px; border-radius: 999px; background: var(--panel); border: 1px solid var(--border); color: var(--muted); }
        .status-dot { width: 9px; height: 9px; border-radius: 50%; background: var(--green); box-shadow: 0 0 14px rgba(89,211,155,.65); }
        .setup-grid { display: grid; grid-template-columns: repeat(2, 1fr); gap: 20px; }
        .setup-grid article, .troubleshooting { padding: 28px; border-radius: 18px; background: var(--panel); border: 1px solid var(--border); }
        pre { overflow-x: auto; padding: 14px; border-radius: 10px; color: #cce0ff; background: #070b14; border: 1px solid #1c2943; }
        code { color: #cce0ff; }
        .troubleshooting { margin-top: 24px; }
        .troubleshooting li { margin: 12px 0; color: var(--muted); }
        .warning-box { margin-top: 24px; padding: 16px; border-radius: 12px; color: #ffe9b5; background: rgba(243,201,105,.08); border: 1px solid rgba(243,201,105,.26); }

        /* Dashboard */
        .app-body { overflow-x: hidden; }
        .app-nav { position: fixed; width: 100%; }
        .dashboard-search { flex: 1; max-width: 620px; display: flex; gap: 8px; margin-left: auto; }
        input, select { width: 100%; min-height: 42px; padding: 0 13px; color: var(--text); background: #0d1424; border: 1px solid var(--border); border-radius: 11px; outline: none; }
        input:focus, select:focus { border-color: var(--blue); box-shadow: 0 0 0 3px rgba(92,124,250,.12); }
        .app-layout { min-height: 100vh; padding-top: 76px; display: grid; grid-template-columns: 230px minmax(0, 1fr); }
        .app-sidebar { position: fixed; top: 76px; bottom: 0; width: 230px; display: flex; flex-direction: column; padding: 22px 14px; background: #090e1b; border-right: 1px solid rgba(147,164,199,.1); }
        .app-sidebar nav { display: grid; gap: 6px; }
        .sidebar-link { padding: 13px 14px; border: 1px solid transparent; border-radius: 10px; text-align: left; color: var(--muted); background: transparent; }
        .sidebar-link:hover, .sidebar-link.active { color: var(--text); background: #121b2f; border-color: #24314d; }
        .sidebar-footer { margin-top: auto; display: flex; gap: 9px; align-items: center; color: var(--muted); font-size: 12px; }
        .dashboard-main { grid-column: 2; width: 100%; padding: 38px; }
        .dashboard-heading { display: flex; align-items: end; justify-content: space-between; gap: 24px; margin-bottom: 24px; }
        .dashboard-heading h1 { margin: 8px 0; font-size: clamp(32px, 4vw, 48px); letter-spacing: -.04em; }
        .dashboard-heading p { color: var(--muted); }
        .metric-row { display: grid; grid-template-columns: repeat(4, 1fr); gap: 14px; margin-bottom: 18px; }
        .metric-row article { display: grid; gap: 7px; padding: 18px; border-radius: 14px; background: var(--panel); border: 1px solid var(--border); }
        .metric-row span { color: var(--muted); font-size: 12px; text-transform: uppercase; letter-spacing: .08em; }
        .metric-row strong { font-size: 24px; }
        .dashboard-grid { display: grid; grid-template-columns: minmax(0, 1fr) 390px; gap: 18px; align-items: start; }
        .feed-panel, .analysis-drawer { background: rgba(10,16,32,.9); border: 1px solid var(--border); border-radius: 18px; }
        .feed-panel { padding: 20px; min-width: 0; }
        .analysis-drawer { position: sticky; top: 96px; padding: 20px; }
        .panel-heading { display: flex; align-items: flex-start; justify-content: space-between; gap: 16px; }
        .panel-heading h2 { margin: 0 0 4px; }
        .panel-heading p { margin: 0; color: var(--muted); font-size: 13px; }
        .live-badge { padding: 7px 10px; border-radius: 999px; color: #bdf5d7; background: rgba(89,211,155,.1); border: 1px solid rgba(89,211,155,.28); font-size: 11px; font-weight: 900; }
        .filter-grid { display: grid; grid-template-columns: 1.3fr 1fr 1fr 1fr; gap: 10px; margin: 20px 0 14px; }
        label { display: grid; gap: 7px; color: var(--muted); font-size: 12px; font-weight: 700; }
        .feed-tabs { display: flex; gap: 8px; margin-bottom: 14px; flex-wrap: wrap; }
        .feed-tab { padding: 9px 13px; border-radius: 999px; border: 1px solid var(--border); background: #11192b; color: var(--muted); }
        .feed-tab.active { color: white; background: linear-gradient(135deg, var(--blue), var(--cyan)); border-color: transparent; }
        .token-list { display: grid; gap: 8px; }
        .token-row { width: 100%; display: grid; grid-template-columns: minmax(170px,1.5fr) repeat(4,minmax(82px,.65fr)) 96px; gap: 10px; align-items: center; padding: 14px; color: var(--text); text-align: left; border-radius: 13px; background: #10182b; border: 1px solid #1f2c49; }
        .token-row:hover, .token-row.selected { border-color: #4f6fd1; background: #121d34; }
        .token-identity { min-width: 0; display: flex; align-items: center; gap: 10px; }
        .token-identity .token-avatar { flex: 0 0 auto; width: 42px; height: 42px; }
        .token-identity div:last-child { min-width: 0; display: grid; gap: 4px; }
        .token-identity strong, .token-identity span { overflow: hidden; text-overflow: ellipsis; white-space: nowrap; }
        .token-identity span, .token-cell span { color: var(--muted); font-size: 11px; }
        .token-cell { display: grid; gap: 4px; }
        .token-cell strong { font-size: 13px; }
        .empty-state { min-height: 420px; display: grid; place-items: center; align-content: center; text-align: center; color: var(--muted); }
        .empty-icon { display: grid; place-items: center; width: 58px; height: 58px; border-radius: 16px; background: rgba(92,124,250,.12); color: var(--blue-2); font-weight: 900; font-size: 24px; }
        .analysis-content { margin-top: 18px; }
        .analysis-token-heading { display: flex; align-items: start; justify-content: space-between; gap: 12px; }
        .analysis-token-heading h3 { margin: 0 0 5px; }
        .analysis-token-heading p { margin: 0; color: var(--muted); }
        .mint-text { overflow-wrap: anywhere; color: var(--muted); font-size: 11px; }
        .analysis-metrics { display: grid; grid-template-columns: repeat(2,1fr); gap: 9px; margin: 16px 0; }
        .analysis-metrics article { display: grid; gap: 5px; padding: 12px; border-radius: 11px; background: var(--panel-2); border: 1px solid var(--border); }
        .analysis-metrics span, .risk-score-block span { color: var(--muted); font-size: 11px; text-transform: uppercase; letter-spacing: .06em; }
        .risk-score-block { display: grid; gap: 8px; padding: 14px; border-radius: 12px; background: var(--panel-2); border: 1px solid var(--border); }
        .risk-score-block strong { font-size: 26px; }
        .risk-track { height: 8px; overflow: hidden; border-radius: 999px; background: #080d18; }
        .risk-track span { display: block; width: 0; height: 100%; background: linear-gradient(90deg, var(--green), var(--amber), var(--red)); transition: width .3s ease; }
        .analysis-summary { margin-top: 14px; padding: 14px; border-radius: 12px; background: #0b1120; border: 1px solid #1d2a45; }
        .analysis-summary h3 { margin: 0 0 8px; font-size: 14px; }
        .analysis-summary p { margin: 0; color: #c5d1ec; font-size: 13px; white-space: pre-line; line-height: 1.55; }
        .flag-list { display: grid; gap: 8px; margin-top: 12px; }
        .flag-item { padding: 10px 12px; border-radius: 10px; background: rgba(243,201,105,.07); border: 1px solid rgba(243,201,105,.18); color: #ffe8ad; font-size: 12px; }
        .analysis-actions { display: grid; grid-template-columns: 1fr 1fr; gap: 8px; margin-top: 14px; }
        .paper-dialog { width: min(460px, calc(100% - 30px)); padding: 0; color: var(--text); background: var(--panel); border: 1px solid var(--border); border-radius: 18px; box-shadow: var(--shadow); }
        .paper-dialog::backdrop { background: rgba(2,5,12,.72); backdrop-filter: blur(5px); }
        .paper-dialog form { position: relative; display: grid; gap: 16px; padding: 28px; }
        .dialog-close { position: absolute; right: 14px; top: 12px; border: 0; background: transparent; color: var(--muted); font-size: 26px; }
        .dialog-actions { display: flex; justify-content: flex-end; gap: 8px; }
        .dialog-feedback { min-height: 22px; color: var(--muted); font-size: 13px; }

        @media (max-width: 1050px) {
          .feature-grid, .advantage-grid { grid-template-columns: repeat(2,1fr); }
          .workflow-grid { grid-template-columns: repeat(2,1fr); }
          .demo-body { grid-template-columns: 1fr; }
          .demo-overlay { width: min(440px,100%); justify-self: center; }
          .dashboard-grid { grid-template-columns: 1fr; }
          .analysis-drawer { position: static; }
          .filter-grid { grid-template-columns: repeat(2,1fr); }
        }
        @media (max-width: 820px) {
          .nav-links { display: none; }
          .nav-actions .button-ghost { display: none; }
          .app-layout { display: block; }
          .app-sidebar { display: none; }
          .dashboard-main { padding: 24px 16px; }
          .dashboard-search { margin-left: 0; }
          .app-nav .brand span:last-child { display: none; }
          .metric-row { grid-template-columns: repeat(2,1fr); }
          .token-row { grid-template-columns: minmax(150px,1.4fr) repeat(2,minmax(80px,.7fr)); }
          .token-row .token-cell:nth-of-type(3), .token-row .token-cell:nth-of-type(4) { display: none; }
          .final-cta { flex-direction: column; align-items: flex-start; }
        }
        @media (max-width: 640px) {
          .section-shell { width: min(100% - 24px,1180px); }
          .site-nav { padding-inline: 12px; gap: 12px; }
          .hero { padding-top: 76px; }
          .hero h1 { font-size: 48px; }
          .hero-copy { font-size: 16px; }
          .demo-body { padding: 14px; }
          .feature-grid, .advantage-grid, .workflow-grid, .setup-grid { grid-template-columns: 1fr; }
          .feature-card, .advantage-grid article { min-height: auto; }
          .final-cta { padding: 28px; }
          .site-footer { padding: 28px 0; flex-wrap: wrap; }
          .site-footer p { width: 100%; order: 3; }
          .dashboard-search { display: none; }
          .dashboard-heading { align-items: flex-start; flex-direction: column; }
          .metric-row, .filter-grid { grid-template-columns: 1fr; }
          .token-row { grid-template-columns: 1fr 90px; }
          .token-row .token-cell:nth-of-type(n+2) { display: none; }
        }
    '''),
    "web_static/site.js": clean(r'''
        (() => {
          const status = document.getElementById('setup-backend-status');
          if (!status) return;
          fetch('/api/status')
            .then((response) => {
              if (!response.ok) throw new Error(`HTTP ${response.status}`);
              return response.json();
            })
            .then((data) => {
              status.textContent = `Backend connected: ${data.backend || 'SOLI AI'} · ${data.timeframe || 'live'}`;
            })
            .catch(() => {
              status.textContent = 'Backend not detected. Start python server.py and refresh this page.';
            });
        })();
    '''),
    "web_static/dashboard.js": clean(r'''
        (() => {
          const state = {
            tokens: [],
            selected: null,
            watchlist: new Map(),
            tab: 'new',
            lastSuccess: null,
          };

          const $ = (id) => document.getElementById(id);
          const tokenList = $('token-list');
          const feedMessage = $('feed-message');
          const dialog = $('paper-dialog');

          function safeNumber(value, fallback = 0) {
            const parsed = Number(value);
            return Number.isFinite(parsed) ? parsed : fallback;
          }

          function money(value) {
            const number = safeNumber(value, NaN);
            if (!Number.isFinite(number)) return '—';
            if (Math.abs(number) < 0.01 && number !== 0) return `$${number.toFixed(8)}`;
            return new Intl.NumberFormat('en-US', { style: 'currency', currency: 'USD', maximumFractionDigits: 2 }).format(number);
          }

          function compact(value) {
            const number = safeNumber(value, NaN);
            if (!Number.isFinite(number)) return '—';
            return new Intl.NumberFormat('en-US', { notation: 'compact', maximumFractionDigits: 1 }).format(number);
          }

          function percent(value) {
            const number = safeNumber(value, NaN);
            if (!Number.isFinite(number)) return '—';
            return `${number >= 0 ? '+' : ''}${number.toFixed(1)}%`;
          }

          function shortMint(mint) {
            if (!mint) return 'No mint';
            return mint.length > 13 ? `${mint.slice(0, 6)}…${mint.slice(-5)}` : mint;
          }

          function normalizeRisk(raw) {
            if (raw === null || raw === undefined || raw === '') return null;
            let value = Number(raw);
            if (!Number.isFinite(value)) return null;
            while (value > 1000) value /= 100;
            if (value > 100) value /= 10;
            return Math.max(0, Math.min(100, Math.round(value)));
          }

          function riskMeta(raw) {
            const score = normalizeRisk(raw);
            if (score === null) return { score: null, label: 'Unknown', className: 'unknown' };
            if (score >= 70) return { score, label: 'Extreme', className: 'extreme' };
            if (score >= 50) return { score, label: 'High', className: 'high' };
            if (score >= 25) return { score, label: 'Medium', className: 'medium' };
            return { score, label: 'Lower', className: 'lower' };
          }

          function tokenAge(token) {
            if (token.age_minutes !== undefined && token.age_minutes !== null) {
              const minutes = safeNumber(token.age_minutes);
              if (minutes < 60) return `${Math.round(minutes)}m`;
              if (minutes < 1440) return `${(minutes / 60).toFixed(1)}h`;
              return `${(minutes / 1440).toFixed(1)}d`;
            }
            return token.age || '—';
          }

          async function api(path) {
            const response = await fetch(path, { cache: 'no-store' });
            const body = await response.json().catch(() => ({}));
            if (!response.ok || body.error) throw new Error(body.error || `Request failed (${response.status})`);
            return body;
          }

          async function checkBackend() {
            try {
              const data = await api('/api/status');
              $('backend-status').textContent = data.backend || 'Backend connected';
            } catch (error) {
              $('backend-status').textContent = 'Backend unavailable';
            }
          }

          async function loadTokens() {
            feedMessage.textContent = 'Loading live Solana tokens…';
            const liquidity = Math.max(0, safeNumber($('min-liquidity').value, 25000));
            const age = Math.max(0, safeNumber($('min-age').value, 10));
            try {
              const data = await api(`/api/find?limit=24&min_liquidity=${encodeURIComponent(liquidity)}&min_age=${encodeURIComponent(age)}`);
              state.tokens = Array.isArray(data.tokens) ? data.tokens : [];
              state.lastSuccess = new Date();
              feedMessage.textContent = `${state.tokens.length} tokens loaded from the current discovery feed.`;
              renderTokens();
              updateMetrics();
            } catch (error) {
              feedMessage.textContent = `Live refresh failed: ${error.message}. Showing the last successful results.`;
              renderTokens();
            }
          }

          function filteredTokens() {
            const query = $('feed-search').value.trim().toLowerCase();
            const sort = $('sort-by').value;
            let tokens = state.tab === 'watchlist' ? Array.from(state.watchlist.values()) : [...state.tokens];
            if (query) {
              tokens = tokens.filter((token) => [token.name, token.token_symbol, token.symbol, token.mint].some((value) => String(value || '').toLowerCase().includes(query)));
            }
            if (state.tab === 'boosted') tokens = tokens.filter((token) => token.boosted || safeNumber(token.active_boosts) > 0);
            tokens.sort((a, b) => {
              if (sort === 'volume') return safeNumber(b.volume_24h) - safeNumber(a.volume_24h);
              if (sort === 'change') return safeNumber(b.price_change_24h) - safeNumber(a.price_change_24h);
              if (sort === 'risk') return (normalizeRisk(a.rug_score) ?? 101) - (normalizeRisk(b.rug_score) ?? 101);
              return safeNumber(b.liquidity_usd) - safeNumber(a.liquidity_usd);
            });
            return tokens;
          }

          function renderTokens() {
            const tokens = filteredTokens();
            tokenList.innerHTML = '';
            if (!tokens.length) {
              tokenList.innerHTML = '<div class="empty-state"><div><h3>No tokens matched</h3><p>Adjust the filters or refresh the discovery feed.</p></div></div>';
              return;
            }
            tokens.forEach((token) => {
              const risk = riskMeta(token.rug_score);
              const row = document.createElement('button');
              row.type = 'button';
              row.className = `token-row${state.selected?.mint === token.mint ? ' selected' : ''}`;
              row.innerHTML = `
                <div class="token-identity">
                  <div class="token-avatar">${String(token.token_symbol || token.name || '?').slice(0, 1).toUpperCase()}</div>
                  <div><strong>${token.name || token.token_symbol || 'Unknown token'}</strong><span>${token.token_symbol || token.symbol || '—'} · ${shortMint(token.mint)}</span></div>
                </div>
                <div class="token-cell"><span>Price</span><strong>${money(token.price_usd)}</strong></div>
                <div class="token-cell"><span>Liquidity</span><strong>$${compact(token.liquidity_usd)}</strong></div>
                <div class="token-cell"><span>24h volume</span><strong>$${compact(token.volume_24h)}</strong></div>
                <div class="token-cell"><span>24h</span><strong class="${safeNumber(token.price_change_24h) >= 0 ? 'positive' : 'negative'}">${percent(token.price_change_24h)}</strong></div>
                <div class="token-cell"><span>Risk</span><strong>${risk.score ?? '—'} · ${risk.label}</strong></div>
              `;
              row.addEventListener('click', () => selectToken(token));
              tokenList.appendChild(row);
            });
          }

          async function selectToken(token) {
            state.selected = token;
            renderTokens();
            $('analysis-empty').classList.add('hidden');
            $('analysis-content').classList.remove('hidden');
            $('analysis-name').textContent = token.name || 'Unknown token';
            $('analysis-symbol').textContent = token.token_symbol || token.symbol || '—';
            $('analysis-mint').textContent = token.mint || 'No mint available';
            $('analysis-price').textContent = money(token.price_usd);
            $('analysis-liquidity').textContent = `$${compact(token.liquidity_usd)}`;
            $('analysis-volume').textContent = `$${compact(token.volume_24h)}`;
            $('analysis-signal').textContent = 'Loading…';
            $('analysis-summary-text').textContent = 'Running the current SOLI AI analysis…';
            $('analysis-flags').innerHTML = '';
            applyRisk(token.rug_score);
            try {
              const data = await api(`/api/check?symbol=${encodeURIComponent(token.mint || token.symbol || '')}`);
              $('analysis-signal').textContent = data.signal || '—';
              $('analysis-summary-text').textContent = data.assistant_summary || 'No written summary was returned.';
              const pair = data.pair_info || {};
              $('analysis-price').textContent = money(pair.priceUsd ?? data.current_price ?? token.price_usd);
              $('analysis-liquidity').textContent = `$${compact((pair.liquidity || {}).usd ?? token.liquidity_usd)}`;
              $('analysis-volume').textContent = `$${compact((pair.volume || {}).h24 ?? token.volume_24h)}`;
              const riskRaw = data.rug_summary?.score ?? token.rug_score;
              applyRisk(riskRaw);
              const flags = data.rug_summary?.flags || token.rug_flags || [];
              renderFlags(flags);
            } catch (error) {
              $('analysis-summary-text').textContent = `Analysis failed: ${error.message}`;
              renderFlags(token.rug_flags || []);
            }
          }

          function applyRisk(raw) {
            const risk = riskMeta(raw);
            $('analysis-risk-score').textContent = risk.score === null ? 'Unknown' : `${risk.score} / 100`;
            $('analysis-risk-bar').style.width = `${risk.score ?? 0}%`;
            const chip = $('analysis-risk-chip');
            chip.textContent = risk.label;
            chip.className = `risk-chip ${risk.className}`;
          }

          function renderFlags(flags) {
            const holder = $('analysis-flags');
            holder.innerHTML = '';
            (Array.isArray(flags) ? flags : []).slice(0, 8).forEach((flag) => {
              const item = document.createElement('div');
              item.className = 'flag-item';
              item.textContent = flag;
              holder.appendChild(item);
            });
          }

          function updateMetrics() {
            $('metric-tokens').textContent = state.tokens.length;
            $('metric-lower-risk').textContent = state.tokens.filter((token) => (normalizeRisk(token.rug_score) ?? 101) < 25).length;
            $('metric-watchlist').textContent = state.watchlist.size;
            $('metric-update').textContent = state.lastSuccess ? state.lastSuccess.toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' }) : '—';
          }

          function openPaperDialog() {
            if (!state.selected) return;
            $('paper-token-label').textContent = `${state.selected.name || 'Token'} · ${shortMint(state.selected.mint)}`;
            $('paper-feedback').textContent = 'This creates a simulated position only.';
            dialog.showModal();
          }

          async function paperBuy() {
            if (!state.selected) return;
            const units = safeNumber($('paper-units').value, 0);
            if (units <= 0) {
              $('paper-feedback').textContent = 'Enter a token-unit amount greater than zero.';
              return;
            }
            $('paper-feedback').textContent = 'Submitting paper trade…';
            try {
              const data = await api(`/api/buy?symbol=${encodeURIComponent(state.selected.mint)}&units=${encodeURIComponent(units)}`);
              $('paper-feedback').textContent = `Paper buy recorded. Portfolio value: ${money(data.portfolio?.portfolio_value)}`;
            } catch (error) {
              $('paper-feedback').textContent = `Paper buy failed: ${error.message}`;
            }
          }

          $('refresh-feed').addEventListener('click', loadTokens);
          $('feed-search').addEventListener('input', renderTokens);
          $('sort-by').addEventListener('change', renderTokens);
          $('min-liquidity').addEventListener('change', loadTokens);
          $('min-age').addEventListener('change', loadTokens);
          document.querySelectorAll('.feed-tab').forEach((button) => button.addEventListener('click', () => {
            document.querySelectorAll('.feed-tab').forEach((item) => item.classList.remove('active'));
            button.classList.add('active');
            state.tab = button.dataset.tab;
            renderTokens();
          }));
          $('analyze-mint').addEventListener('click', () => {
            const mint = $('global-mint').value.trim();
            if (!mint) return;
            selectToken({ mint, name: 'Manual token', token_symbol: shortMint(mint) });
          });
          $('global-mint').addEventListener('keydown', (event) => {
            if (event.key === 'Enter') $('analyze-mint').click();
          });
          $('watch-token').addEventListener('click', () => {
            if (!state.selected?.mint) return;
            if (state.watchlist.has(state.selected.mint)) {
              state.watchlist.delete(state.selected.mint);
              $('watch-token').textContent = 'Add to watchlist';
            } else {
              state.watchlist.set(state.selected.mint, state.selected);
              $('watch-token').textContent = 'Remove from watchlist';
            }
            updateMetrics();
          });
          $('paper-buy-token').addEventListener('click', openPaperDialog);
          $('confirm-paper-buy').addEventListener('click', paperBuy);

          checkBackend();
          loadTokens();
          setInterval(loadTokens, 20000);
        })();
    '''),
    "extension/manifest.json": json.dumps({
        "manifest_version": 3,
        "name": "SOLI AI Overlay",
        "version": "0.1.0",
        "description": "Local SOLI AI token-analysis and paper-trading overlay for Axiom.",
        "permissions": ["storage", "activeTab", "tabs"],
        "host_permissions": [
            "https://axiom.trade/*",
            "https://*.axiom.trade/*",
            "http://127.0.0.1:5500/*",
            "http://localhost:5500/*"
        ],
        "background": {"service_worker": "background.js"},
        "action": {"default_title": "SOLI AI", "default_popup": "popup.html"},
        "content_scripts": [{
            "matches": ["https://axiom.trade/*", "https://*.axiom.trade/*"],
            "js": ["content.js"],
            "run_at": "document_idle"
        }]
    }, indent=2),
    "extension/background.js": clean(r'''
        const API_BASE = 'http://127.0.0.1:5500';

        chrome.runtime.onMessage.addListener((message, sender, sendResponse) => {
          if (message?.type === 'soli-api') {
            const path = String(message.path || '');
            if (!path.startsWith('/api/')) {
              sendResponse({ ok: false, error: 'Invalid API path.' });
              return false;
            }
            fetch(`${API_BASE}${path}`, { method: 'GET', cache: 'no-store' })
              .then(async (response) => {
                const data = await response.json().catch(() => ({}));
                if (!response.ok || data.error) throw new Error(data.error || `HTTP ${response.status}`);
                sendResponse({ ok: true, data });
              })
              .catch((error) => sendResponse({ ok: false, error: error.message }));
            return true;
          }

          if (message?.type === 'soli-toggle') {
            chrome.tabs.query({ active: true, currentWindow: true }, (tabs) => {
              const tab = tabs[0];
              if (!tab?.id) {
                sendResponse({ ok: false, error: 'No active tab.' });
                return;
              }
              chrome.tabs.sendMessage(tab.id, { type: 'soli-toggle-panel', enabled: message.enabled }, () => {
                const error = chrome.runtime.lastError;
                sendResponse(error ? { ok: false, error: error.message } : { ok: true });
              });
            });
            return true;
          }

          return false;
        });
    '''),
    "extension/popup.html": clean(r'''
        <!doctype html>
        <html lang="en">
        <head>
          <meta charset="utf-8">
          <meta name="viewport" content="width=device-width, initial-scale=1">
          <title>SOLI AI</title>
          <style>
            :root{color-scheme:dark}*{box-sizing:border-box}body{width:300px;margin:0;padding:18px;background:#0b1120;color:#f5f7ff;font-family:Inter,system-ui,sans-serif}.brand{display:flex;align-items:center;gap:10px;font-weight:800}.mark{display:grid;place-items:center;width:34px;height:34px;border-radius:10px;background:linear-gradient(135deg,#5c7cfa,#54c8e8)}p{color:#93a4c7;line-height:1.5;font-size:13px}.row{display:flex;align-items:center;justify-content:space-between;padding:13px 0;border-top:1px solid #24314d}.switch{position:relative;width:44px;height:24px}.switch input{opacity:0;width:0;height:0}.slider{position:absolute;inset:0;border-radius:999px;background:#25324f}.slider:before{content:"";position:absolute;width:18px;height:18px;left:3px;top:3px;border-radius:50%;background:white;transition:.2s}.switch input:checked+.slider{background:#5c7cfa}.switch input:checked+.slider:before{transform:translateX(20px)}button{width:100%;min-height:40px;border-radius:10px;border:1px solid #2b3d63;background:#121b2f;color:white;font-weight:700;cursor:pointer}#status{min-height:18px;font-size:12px;color:#93a4c7}
          </style>
        </head>
        <body>
          <div class="brand"><span class="mark">S</span><span>SOLI AI</span></div>
          <p>Control the local SOLI AI overlay on the current Axiom tab.</p>
          <div class="row"><span>Show overlay</span><label class="switch"><input id="enabled" type="checkbox" checked><span class="slider"></span></label></div>
          <button id="health" type="button">Check local backend</button>
          <p id="status" aria-live="polite"></p>
          <script src="popup.js"></script>
        </body>
        </html>
    '''),
    "extension/popup.js": clean(r'''
        const enabled = document.getElementById('enabled');
        const status = document.getElementById('status');

        chrome.storage.local.get({ enabled: true }, (settings) => {
          enabled.checked = settings.enabled;
        });

        enabled.addEventListener('change', () => {
          chrome.storage.local.set({ enabled: enabled.checked });
          chrome.runtime.sendMessage({ type: 'soli-toggle', enabled: enabled.checked }, (response) => {
            status.textContent = response?.ok ? 'Overlay setting updated.' : (response?.error || 'Open an Axiom tab and try again.');
          });
        });

        document.getElementById('health').addEventListener('click', () => {
          status.textContent = 'Checking backend…';
          chrome.runtime.sendMessage({ type: 'soli-api', path: '/api/status' }, (response) => {
            status.textContent = response?.ok ? `Connected: ${response.data.backend || 'SOLI AI'}` : `Unavailable: ${response?.error || 'Unknown error'}`;
          });
        });
    '''),
    "extension/content.js": clean(r'''
        (() => {
          if (window.__SOLI_AI_OVERLAY_LOADED__) return;
          window.__SOLI_AI_OVERLAY_LOADED__ = true;

          const DEFAULTS = {
            enabled: true,
            opacity: 100,
            refreshSeconds: 10,
            scale: 100,
            locked: false,
            autoRefresh: true,
            compact: false,
            sound: false,
            x: Math.max(20, window.innerWidth - 490),
            y: 90,
          };

          const state = {
            settings: { ...DEFAULTS },
            mint: '',
            currentView: 'menu',
            analysis: null,
            tokens: [],
            refreshTimer: null,
            visible: true,
          };

          const BASE58_RE = /\b[1-9A-HJ-NP-Za-km-z]{32,44}\b/g;
          let host;
          let root;

          function api(path) {
            return new Promise((resolve, reject) => {
              chrome.runtime.sendMessage({ type: 'soli-api', path }, (response) => {
                const error = chrome.runtime.lastError;
                if (error) return reject(new Error(error.message));
                if (!response?.ok) return reject(new Error(response?.error || 'SOLI AI backend request failed.'));
                resolve(response.data);
              });
            });
          }

          function escapeHtml(value) {
            return String(value ?? '')
              .replaceAll('&', '&amp;')
              .replaceAll('<', '&lt;')
              .replaceAll('>', '&gt;')
              .replaceAll('"', '&quot;')
              .replaceAll("'", '&#039;');
          }

          function shortMint(mint) {
            return mint && mint.length > 14 ? `${mint.slice(0, 7)}…${mint.slice(-6)}` : (mint || 'No token detected');
          }

          function safeNumber(value, fallback = 0) {
            const parsed = Number(value);
            return Number.isFinite(parsed) ? parsed : fallback;
          }

          function money(value) {
            const number = Number(value);
            if (!Number.isFinite(number)) return '—';
            if (Math.abs(number) < .01 && number !== 0) return `$${number.toFixed(8)}`;
            return new Intl.NumberFormat('en-US', { style: 'currency', currency: 'USD', maximumFractionDigits: 2 }).format(number);
          }

          function compact(value) {
            const number = Number(value);
            if (!Number.isFinite(number)) return '—';
            return new Intl.NumberFormat('en-US', { notation: 'compact', maximumFractionDigits: 1 }).format(number);
          }

          function normalizeRisk(raw) {
            if (raw === null || raw === undefined || raw === '') return null;
            let value = Number(raw);
            if (!Number.isFinite(value)) return null;
            while (value > 1000) value /= 100;
            if (value > 100) value /= 10;
            return Math.max(0, Math.min(100, Math.round(value)));
          }

          function riskMeta(raw) {
            const score = normalizeRisk(raw);
            if (score === null) return { score: null, label: 'Unknown', cls: 'unknown' };
            if (score >= 70) return { score, label: 'Extreme risk', cls: 'extreme' };
            if (score >= 50) return { score, label: 'High risk', cls: 'high' };
            if (score >= 25) return { score, label: 'Medium risk', cls: 'medium' };
            return { score, label: 'Lower observed risk', cls: 'lower' };
          }

          function detectMint() {
            const candidates = [];
            try {
              const url = new URL(location.href);
              candidates.push(...(url.pathname.match(BASE58_RE) || []));
              url.searchParams.forEach((value) => candidates.push(...(String(value).match(BASE58_RE) || [])));
            } catch (_) {}

            document.querySelectorAll('a[href]').forEach((link) => {
              if (candidates.length > 20) return;
              candidates.push(...(link.href.match(BASE58_RE) || []));
            });

            const bodyText = document.body?.innerText?.slice(0, 180000) || '';
            candidates.push(...(bodyText.match(BASE58_RE) || []));

            return candidates.find((candidate) => !candidate.startsWith('111111')) || '';
          }

          function saveSettings() {
            chrome.storage.local.set({ soliSettings: state.settings });
          }

          function applySettings() {
            if (!host) return;
            host.style.opacity = String(state.settings.opacity / 100);
            host.style.transform = `scale(${state.settings.scale / 100})`;
            host.style.transformOrigin = 'top left';
            host.style.left = `${Math.max(0, state.settings.x)}px`;
            host.style.top = `${Math.max(0, state.settings.y)}px`;
            host.classList.toggle('soli-compact-host', state.settings.compact);
          }

          function mount() {
            host = document.createElement('div');
            host.id = 'soli-ai-overlay-host';
            document.documentElement.appendChild(host);
            root = host.attachShadow({ mode: 'open' });

            const styleLink = document.createElement('link');
            styleLink.rel = 'stylesheet';
            styleLink.href = chrome.runtime.getURL('overlay.css');
            root.appendChild(styleLink);

            const shell = document.createElement('section');
            shell.className = 'soli-panel';
            shell.innerHTML = `
              <header class="soli-header" id="soli-drag-handle">
                <button class="soli-collapse" id="soli-collapse" type="button" aria-label="Collapse panel">⌃</button>
                <strong>SOLI AI</strong>
                <span class="soli-live-dot" title="Local backend status"></span>
              </header>
              <div class="soli-body" id="soli-body"></div>
            `;
            root.appendChild(shell);
            wireShell();
            applySettings();
            renderMenu();
            makeDraggable(root.getElementById('soli-drag-handle'));
            backendHealth();
          }

          function wireShell() {
            root.getElementById('soli-collapse').addEventListener('click', () => {
              root.querySelector('.soli-panel').classList.toggle('collapsed');
            });
          }

          function makeDraggable(handle) {
            let active = false;
            let startX = 0;
            let startY = 0;
            let originX = 0;
            let originY = 0;

            handle.addEventListener('pointerdown', (event) => {
              if (state.settings.locked || event.target.closest('button')) return;
              active = true;
              startX = event.clientX;
              startY = event.clientY;
              originX = state.settings.x;
              originY = state.settings.y;
              handle.setPointerCapture(event.pointerId);
            });

            handle.addEventListener('pointermove', (event) => {
              if (!active) return;
              state.settings.x = Math.max(0, originX + event.clientX - startX);
              state.settings.y = Math.max(0, originY + event.clientY - startY);
              applySettings();
            });

            handle.addEventListener('pointerup', () => {
              if (!active) return;
              active = false;
              saveSettings();
            });
          }

          function setBody(html) {
            root.getElementById('soli-body').innerHTML = html;
          }

          function header(title) {
            return `<div class="soli-view-header"><button id="soli-back" type="button">‹</button><strong>${escapeHtml(title)}</strong></div>`;
          }

          function bindBack() {
            root.getElementById('soli-back')?.addEventListener('click', renderMenu);
          }

          function renderMenu() {
            state.currentView = 'menu';
            clearRefresh();
            setBody(`
              <div class="soli-token-strip">
                <span>Detected token</span>
                <strong>${escapeHtml(shortMint(state.mint))}</strong>
              </div>
              <nav class="soli-menu">
                <button data-view="analysis" type="button"><span>AI</span><div><strong>AI Token Analysis</strong><small>Market context and signals</small></div></button>
                <button data-view="risk" type="button"><span>R</span><div><strong>Rug Pull Detector</strong><small>Authorities, holders, liquidity</small></div></button>
                <button data-view="finder" type="button"><span>F</span><div><strong>Token Finder</strong><small>New and trending Solana tokens</small></div></button>
                <button data-view="paper" type="button"><span>P</span><div><strong>Paper Trading</strong><small>Simulated entries and exits</small></div></button>
                <button data-view="portfolio" type="button"><span>$</span><div><strong>Portfolio</strong><small>Current paper position</small></div></button>
                <button data-view="settings" type="button"><span>⚙</span><div><strong>Settings</strong><small>Panel and refresh preferences</small></div></button>
              </nav>
              <div class="soli-manual-mint">
                <label for="soli-mint-input">Manual mint</label>
                <div><input id="soli-mint-input" value="${escapeHtml(state.mint)}" placeholder="Paste Solana mint"><button id="soli-use-mint" type="button">Use</button></div>
              </div>
            `);
            root.querySelectorAll('[data-view]').forEach((button) => button.addEventListener('click', () => openView(button.dataset.view)));
            root.getElementById('soli-use-mint').addEventListener('click', () => {
              const mint = root.getElementById('soli-mint-input').value.trim();
              if (mint) {
                state.mint = mint;
                renderMenu();
              }
            });
          }

          function openView(view) {
            state.currentView = view;
            if (view === 'analysis') return renderAnalysis();
            if (view === 'risk') return renderRisk();
            if (view === 'finder') return renderFinder();
            if (view === 'paper') return renderPaper();
            if (view === 'portfolio') return renderPortfolio();
            if (view === 'settings') return renderSettings();
          }

          function noMintView(title) {
            setBody(`${header(title)}<div class="soli-empty"><div class="soli-empty-icon">S</div><h2>Ready to analyze</h2><p>Open a token page on Axiom or paste a Solana mint from the main menu.</p></div>`);
            bindBack();
          }

          async function loadAnalysis() {
            if (!state.mint) return;
            const data = await api(`/api/check?symbol=${encodeURIComponent(state.mint)}`);
            state.analysis = data;
            return data;
          }

          async function renderAnalysis() {
            if (!state.mint) return noMintView('AI Token Analysis');
            setBody(`${header('AI Token Analysis')}<div class="soli-loading"><span></span><p>Analyzing ${escapeHtml(shortMint(state.mint))}…</p></div>`);
            bindBack();
            try {
              const data = await loadAnalysis();
              const pair = data.pair_info || {};
              const base = pair.baseToken || {};
              const risk = riskMeta(data.rug_summary?.score);
              const flags = data.rug_summary?.flags || [];
              setBody(`
                ${header('AI Token Analysis')}
                <div class="soli-token-heading"><div class="soli-avatar">${escapeHtml((base.symbol || '?').slice(0,1))}</div><div><h2>${escapeHtml(base.name || 'Solana token')}</h2><p>${escapeHtml(base.symbol || shortMint(state.mint))}</p></div><span class="soli-risk ${risk.cls}">${escapeHtml(risk.label)}</span></div>
                <div class="soli-metric-grid">
                  <article><span>Price</span><strong>${money(pair.priceUsd ?? data.current_price)}</strong></article>
                  <article><span>Liquidity</span><strong>$${compact(pair.liquidity?.usd)}</strong></article>
                  <article><span>24h volume</span><strong>$${compact(pair.volume?.h24)}</strong></article>
                  <article><span>Signal</span><strong>${escapeHtml(data.signal || '—')}</strong></article>
                </div>
                <div class="soli-score"><div><span>Observed risk</span><strong>${risk.score === null ? 'Unknown' : `${risk.score} / 100`}</strong></div><div class="soli-score-track"><span style="width:${risk.score ?? 0}%"></span></div></div>
                <section class="soli-summary"><h3>SOLI AI summary</h3><p>${escapeHtml(data.assistant_summary || 'No summary returned.')}</p></section>
                <div class="soli-flags">${flags.slice(0,6).map((flag) => `<div>⚠ ${escapeHtml(flag)}</div>`).join('') || '<div>No risk flags were returned.</div>'}</div>
                <div class="soli-actions"><button id="soli-analysis-paper" type="button">Paper buy</button><button id="soli-refresh-analysis" class="secondary" type="button">Refresh</button></div>
              `);
              bindBack();
              root.getElementById('soli-analysis-paper').addEventListener('click', renderPaper);
              root.getElementById('soli-refresh-analysis').addEventListener('click', renderAnalysis);
              scheduleRefresh(renderAnalysis);
            } catch (error) {
              renderError('AI Token Analysis', error);
            }
          }

          async function renderRisk() {
            if (!state.mint) return noMintView('Rug Pull Detector');
            setBody(`${header('Rug Pull Detector')}<div class="soli-loading"><span></span><p>Running contract and holder checks…</p></div>`);
            bindBack();
            try {
              const data = state.analysis?.symbol === state.mint ? state.analysis : await loadAnalysis();
              const risk = riskMeta(data.rug_summary?.score);
              const flags = data.rug_summary?.flags || [];
              setBody(`
                ${header('Rug Pull Detector')}
                <div class="soli-risk-hero ${risk.cls}"><span>Observed risk</span><strong>${risk.score === null ? 'Unknown' : `${risk.score} / 100`}</strong><b>${escapeHtml(risk.label)}</b></div>
                <div class="soli-check-list">${flags.slice(0,10).map((flag) => `<div><span>⚠</span><p>${escapeHtml(flag)}</p></div>`).join('') || '<div><span>•</span><p>No detailed risk flags were returned.</p></div>'}</div>
                <div class="soli-disclaimer">A low score cannot prove that a token is safe. Pools, lockers, exchanges, and program-owned accounts can distort holder data.</div>
                <button id="soli-risk-refresh" class="soli-primary-full" type="button">Run scan again</button>
              `);
              bindBack();
              root.getElementById('soli-risk-refresh').addEventListener('click', renderRisk);
            } catch (error) {
              renderError('Rug Pull Detector', error);
            }
          }

          async function renderFinder() {
            setBody(`${header('Token Finder')}<div class="soli-finder-intro"><h2>AI Token Discovery Engine</h2><p>Filter public Solana discovery data by liquidity and age, then inspect each token before acting.</p><label>Minimum liquidity<input id="soli-find-liquidity" type="number" value="25000"></label><label>Minimum age (minutes)<input id="soli-find-age" type="number" value="10"></label><button id="soli-launch-scan" class="soli-primary-full" type="button">Launch scan</button></div><div id="soli-finder-results"></div>`);
            bindBack();
            root.getElementById('soli-launch-scan').addEventListener('click', runFinder);
          }

          async function runFinder() {
            const results = root.getElementById('soli-finder-results');
            const liquidity = Math.max(0, safeNumber(root.getElementById('soli-find-liquidity').value, 25000));
            const age = Math.max(0, safeNumber(root.getElementById('soli-find-age').value, 10));
            results.innerHTML = '<div class="soli-loading"><span></span><p>Scanning current Solana tokens…</p></div>';
            try {
              const data = await api(`/api/find?limit=12&min_liquidity=${encodeURIComponent(liquidity)}&min_age=${encodeURIComponent(age)}`);
              state.tokens = Array.isArray(data.tokens) ? data.tokens : [];
              results.innerHTML = `<div class="soli-result-list">${state.tokens.map((token) => {
                const risk = riskMeta(token.rug_score);
                return `<button type="button" data-mint="${escapeHtml(token.mint)}"><div><strong>${escapeHtml(token.name || token.token_symbol || 'Unknown')}</strong><span>${escapeHtml(token.token_symbol || '')} · ${escapeHtml(shortMint(token.mint))}</span></div><div><strong>$${compact(token.liquidity_usd)}</strong><span class="soli-risk ${risk.cls}">${escapeHtml(risk.label)}</span></div></button>`;
              }).join('') || '<p>No tokens matched the current filters.</p>'}</div>`;
              root.querySelectorAll('[data-mint]').forEach((button) => button.addEventListener('click', () => {
                state.mint = button.dataset.mint;
                renderAnalysis();
              }));
            } catch (error) {
              results.innerHTML = `<div class="soli-error">${escapeHtml(error.message)}</div>`;
            }
          }

          function renderPaper() {
            if (!state.mint) return noMintView('Paper Trading');
            setBody(`
              ${header('Paper Trading')}
              <div class="soli-paper-card">
                <span>PAPER MODE</span>
                <h2>${escapeHtml(shortMint(state.mint))}</h2>
                <p>This calls the existing local paper-trading endpoint. It does not submit a wallet transaction.</p>
                <label>Token units<input id="soli-paper-units" type="number" min="0.000001" step="any" value="1"></label>
                <button id="soli-paper-buy" class="soli-primary-full" type="button">Simulate buy</button>
                <button id="soli-paper-sell" class="soli-secondary-full" type="button">Simulate full sell</button>
                <div id="soli-paper-result" class="soli-inline-result"></div>
              </div>
            `);
            bindBack();
            root.getElementById('soli-paper-buy').addEventListener('click', async () => {
              const units = safeNumber(root.getElementById('soli-paper-units').value, 0);
              trade(`/api/buy?symbol=${encodeURIComponent(state.mint)}&units=${encodeURIComponent(units)}`);
            });
            root.getElementById('soli-paper-sell').addEventListener('click', () => trade(`/api/sell?symbol=${encodeURIComponent(state.mint)}`));
          }

          async function trade(path) {
            const result = root.getElementById('soli-paper-result');
            result.textContent = 'Submitting paper trade…';
            try {
              const data = await api(path);
              result.textContent = `${data.action || 'Trade'} recorded. Portfolio value: ${money(data.portfolio?.portfolio_value)}`;
            } catch (error) {
              result.textContent = `Paper trade failed: ${error.message}`;
            }
          }

          async function renderPortfolio() {
            if (!state.mint) return noMintView('Portfolio');
            setBody(`${header('Portfolio')}<div class="soli-loading"><span></span><p>Loading paper portfolio…</p></div>`);
            bindBack();
            try {
              const data = await api(`/api/portfolio?symbol=${encodeURIComponent(state.mint)}`);
              setBody(`
                ${header('Portfolio')}
                <div class="soli-portfolio-value"><span>Paper portfolio value</span><strong>${money(data.portfolio_value)}</strong><small>${escapeHtml(shortMint(state.mint))}</small></div>
                <div class="soli-metric-grid">
                  <article><span>Cash</span><strong>${money(data.cash)}</strong></article>
                  <article><span>Position units</span><strong>${compact(data.position_units)}</strong></article>
                  <article><span>Entry price</span><strong>${money(data.entry_price)}</strong></article>
                  <article><span>Current price</span><strong>${money(data.current_price)}</strong></article>
                </div>
                <h3 class="soli-section-title">Recent paper trades</h3>
                <div class="soli-trades">${(data.recent_trades || []).slice(0,6).map((trade) => `<div><strong>${escapeHtml(String(trade.side || trade.action || 'trade').toUpperCase())}</strong><span>${money(trade.price)} · ${compact(trade.units)} units</span></div>`).join('') || '<p>No paper trades recorded.</p>'}</div>
              `);
              bindBack();
            } catch (error) {
              renderError('Portfolio', error);
            }
          }

          function renderSettings() {
            const s = state.settings;
            setBody(`
              ${header('Settings')}
              <div class="soli-settings">
                <label>Panel opacity <output id="soli-opacity-output">${s.opacity}%</output><input id="soli-opacity" type="range" min="45" max="100" value="${s.opacity}"></label>
                <label>Refresh rate <output id="soli-refresh-output">${s.refreshSeconds}s</output><input id="soli-refresh" type="range" min="3" max="60" value="${s.refreshSeconds}"></label>
                <label>Panel size <output id="soli-scale-output">${s.scale}%</output><input id="soli-scale" type="range" min="70" max="125" value="${s.scale}"></label>
                ${toggle('soli-lock', 'Lock panel position', s.locked)}
                ${toggle('soli-auto', 'Auto-refresh analysis', s.autoRefresh)}
                ${toggle('soli-compact', 'Compact mode', s.compact)}
                ${toggle('soli-sound', 'Sound notifications', s.sound)}
                <button id="soli-reset-settings" class="soli-secondary-full" type="button">Reset panel settings</button>
              </div>
            `);
            bindBack();
            bindRange('soli-opacity', 'soli-opacity-output', 'opacity', '%');
            bindRange('soli-refresh', 'soli-refresh-output', 'refreshSeconds', 's');
            bindRange('soli-scale', 'soli-scale-output', 'scale', '%');
            bindToggle('soli-lock', 'locked');
            bindToggle('soli-auto', 'autoRefresh');
            bindToggle('soli-compact', 'compact');
            bindToggle('soli-sound', 'sound');
            root.getElementById('soli-reset-settings').addEventListener('click', () => {
              state.settings = { ...DEFAULTS };
              saveSettings();
              applySettings();
              renderSettings();
            });
          }

          function toggle(id, label, checked) {
            return `<label class="soli-toggle-row"><span>${escapeHtml(label)}</span><input id="${id}" type="checkbox" ${checked ? 'checked' : ''}><i></i></label>`;
          }

          function bindRange(id, outputId, key, suffix) {
            const input = root.getElementById(id);
            const output = root.getElementById(outputId);
            input.addEventListener('input', () => {
              state.settings[key] = Number(input.value);
              output.textContent = `${input.value}${suffix}`;
              applySettings();
              saveSettings();
            });
          }

          function bindToggle(id, key) {
            root.getElementById(id).addEventListener('change', (event) => {
              state.settings[key] = event.target.checked;
              applySettings();
              saveSettings();
            });
          }

          function renderError(title, error) {
            setBody(`${header(title)}<div class="soli-error"><strong>Unable to load this view</strong><p>${escapeHtml(error.message)}</p><p>Confirm that <code>python server.py</code> is running on port 5500.</p></div>`);
            bindBack();
          }

          async function backendHealth() {
            try {
              await api('/api/status');
              root.querySelector('.soli-live-dot')?.classList.add('online');
            } catch (_) {
              root.querySelector('.soli-live-dot')?.classList.remove('online');
            }
          }

          function scheduleRefresh(callback) {
            clearRefresh();
            if (!state.settings.autoRefresh) return;
            state.refreshTimer = setTimeout(() => {
              if (state.currentView === 'analysis') callback();
            }, state.settings.refreshSeconds * 1000);
          }

          function clearRefresh() {
            if (state.refreshTimer) clearTimeout(state.refreshTimer);
            state.refreshTimer = null;
          }

          function watchNavigation() {
            let lastUrl = location.href;
            const update = () => {
              const next = detectMint();
              if (next && next !== state.mint) {
                state.mint = next;
                state.analysis = null;
                if (state.currentView === 'analysis' || state.currentView === 'risk') openView(state.currentView);
                else renderMenu();
              }
            };
            const observer = new MutationObserver(() => {
              if (location.href !== lastUrl) {
                lastUrl = location.href;
                setTimeout(update, 350);
              }
            });
            observer.observe(document.documentElement, { childList: true, subtree: true });
            window.addEventListener('popstate', () => setTimeout(update, 250));
            setInterval(update, 5000);
            update();
          }

          chrome.runtime.onMessage.addListener((message) => {
            if (message?.type === 'soli-toggle-panel') {
              state.visible = Boolean(message.enabled);
              host.style.display = state.visible ? 'block' : 'none';
            }
          });

          chrome.storage.local.get({ enabled: true, soliSettings: DEFAULTS }, (saved) => {
            state.settings = { ...DEFAULTS, ...(saved.soliSettings || {}) };
            state.visible = saved.enabled !== false;
            mount();
            host.style.display = state.visible ? 'block' : 'none';
            watchNavigation();
          });
        })();
    '''),
    "extension/overlay.css": clean(r'''
        :host { all: initial; }
        * { box-sizing: border-box; }
        .soli-panel { width: 440px; max-height: min(720px, calc(100vh - 24px)); overflow: hidden; resize: both; color: #f5f7ff; background: #101622; border: 1px solid #38507f; border-radius: 16px; box-shadow: 0 24px 80px rgba(0,0,0,.58); font-family: Inter, ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif; }
        .soli-panel.collapsed { height: 46px !important; resize: none; }
        .soli-panel.collapsed .soli-body { display: none; }
        .soli-header { height: 46px; display: grid; grid-template-columns: 38px 1fr 38px; align-items: center; padding: 0 8px; color: #77a1ff; background: linear-gradient(180deg,#151d2b,#111722); border-bottom: 1px solid #2e436e; cursor: move; user-select: none; }
        .soli-header strong { text-align: center; font-size: 13px; letter-spacing: .04em; }
        .soli-collapse { width: 30px; height: 30px; border: 0; color: #9cb6e8; background: transparent; border-radius: 8px; cursor: pointer; }
        .soli-collapse:hover { background: #1b263b; }
        .soli-live-dot { justify-self: center; width: 9px; height: 9px; border-radius: 50%; background: #58647a; }
        .soli-live-dot.online { background: #59d39b; box-shadow: 0 0 12px rgba(89,211,155,.7); }
        .soli-body { max-height: calc(min(720px, 100vh - 24px) - 46px); overflow: auto; background: #101622; }
        .soli-body::-webkit-scrollbar { width: 8px; }
        .soli-body::-webkit-scrollbar-thumb { border-radius: 999px; background: #35415a; }
        button, input { font: inherit; }
        button { cursor: pointer; }
        .soli-view-header { height: 50px; display: grid; grid-template-columns: 38px 1fr; align-items: center; padding: 0 12px; border-bottom: 1px solid #252f42; }
        .soli-view-header button { border: 0; background: transparent; color: #9eb3d9; font-size: 28px; }
        .soli-view-header strong { color: #79a4ff; font-size: 14px; }
        .soli-token-strip { display: flex; justify-content: space-between; gap: 14px; padding: 14px 18px; color: #9eabc2; background: #0d131e; border-bottom: 1px solid #222d42; font-size: 12px; }
        .soli-token-strip strong { color: #d9e4ff; }
        .soli-menu { display: grid; padding: 10px; }
        .soli-menu button { width: 100%; display: grid; grid-template-columns: 38px 1fr; gap: 11px; align-items: center; padding: 12px; text-align: left; color: #eff4ff; border: 1px solid transparent; border-radius: 10px; background: transparent; }
        .soli-menu button:hover { background: #151e2d; border-color: #273b61; }
        .soli-menu button > span { display: grid; place-items: center; width: 34px; height: 34px; color: #79a4ff; border-radius: 9px; background: #172238; border: 1px solid #293e66; font-weight: 800; }
        .soli-menu button div { display: grid; gap: 3px; }
        .soli-menu small { color: #8d9ab2; }
        .soli-manual-mint { display: grid; gap: 7px; padding: 14px 18px 18px; border-top: 1px solid #222d42; }
        .soli-manual-mint label, .soli-finder-intro label, .soli-paper-card label, .soli-settings > label:not(.soli-toggle-row) { display: grid; gap: 8px; color: #aab5ca; font-size: 12px; }
        .soli-manual-mint div { display: grid; grid-template-columns: 1fr auto; gap: 7px; }
        input { width: 100%; min-height: 40px; padding: 0 11px; color: #f5f7ff; background: #0c121d; border: 1px solid #2b3a59; border-radius: 9px; outline: none; }
        input:focus { border-color: #5c7cfa; box-shadow: 0 0 0 3px rgba(92,124,250,.12); }
        .soli-manual-mint button { padding: 0 14px; color: white; background: #263b69; border: 1px solid #4564a6; border-radius: 9px; }
        .soli-empty { min-height: 260px; display: grid; justify-items: center; align-content: center; padding: 30px; text-align: center; }
        .soli-empty-icon { display: grid; place-items: center; width: 54px; height: 54px; border-radius: 15px; color: #81a8ff; background: #172238; border: 1px solid #304b7d; font-size: 22px; font-weight: 900; }
        .soli-empty h2 { margin: 18px 0 8px; color: #78a2ff; }
        .soli-empty p { max-width: 320px; margin: 0; color: #aeb8ca; line-height: 1.65; }
        .soli-loading { min-height: 220px; display: grid; place-items: center; align-content: center; gap: 16px; color: #a9b5cb; }
        .soli-loading span { width: 28px; height: 28px; border: 3px solid #29354c; border-top-color: #6f91ff; border-radius: 50%; animation: soli-spin .8s linear infinite; }
        @keyframes soli-spin { to { transform: rotate(360deg); } }
        .soli-token-heading { display: grid; grid-template-columns: 52px 1fr auto; gap: 12px; align-items: center; padding: 18px; }
        .soli-avatar { display: grid; place-items: center; width: 52px; height: 52px; border-radius: 13px; color: #dce7ff; background: #1a2741; border: 1px solid #365387; font-size: 20px; font-weight: 900; }
        .soli-token-heading h2 { margin: 0 0 4px; font-size: 18px; }
        .soli-token-heading p { margin: 0; color: #91a0ba; }
        .soli-risk { display: inline-flex; justify-content: center; padding: 6px 8px; border-radius: 999px; font-size: 10px; font-weight: 800; }
        .soli-risk.lower { color: #bff4d9; background: rgba(89,211,155,.14); }
        .soli-risk.medium { color: #ffe8a8; background: rgba(243,201,105,.14); }
        .soli-risk.high, .soli-risk.extreme { color: #ffd0d6; background: rgba(239,127,143,.16); }
        .soli-risk.unknown { color: #d7e0f4; background: rgba(147,164,199,.13); }
        .soli-metric-grid { display: grid; grid-template-columns: repeat(2,1fr); gap: 9px; padding: 0 18px 14px; }
        .soli-metric-grid article { display: grid; gap: 5px; padding: 12px; background: #151e2e; border: 1px solid #263754; border-radius: 10px; }
        .soli-metric-grid span, .soli-score span, .soli-portfolio-value span { color: #8f9cb4; font-size: 10px; text-transform: uppercase; letter-spacing: .07em; }
        .soli-score { display: grid; gap: 9px; margin: 0 18px 14px; padding: 13px; background: #151e2e; border: 1px solid #263754; border-radius: 10px; }
        .soli-score > div:first-child { display: flex; justify-content: space-between; align-items: center; }
        .soli-score-track { height: 8px; overflow: hidden; border-radius: 999px; background: #080d16; }
        .soli-score-track span { display: block; height: 100%; background: linear-gradient(90deg,#59d39b,#f3c969,#ef7f8f); }
        .soli-summary { margin: 0 18px 12px; padding: 13px; background: #0c121d; border: 1px solid #202e48; border-radius: 10px; }
        .soli-summary h3 { margin: 0 0 8px; color: #77a1ff; font-size: 13px; }
        .soli-summary p { margin: 0; color: #c7d0e1; white-space: pre-line; line-height: 1.55; font-size: 12px; }
        .soli-flags { display: grid; gap: 7px; padding: 0 18px 14px; }
        .soli-flags div { padding: 9px 10px; color: #ffe2a1; background: rgba(243,201,105,.06); border: 1px solid rgba(243,201,105,.16); border-radius: 9px; font-size: 11px; }
        .soli-actions { display: grid; grid-template-columns: 1fr 1fr; gap: 8px; padding: 0 18px 18px; }
        .soli-actions button, .soli-primary-full, .soli-secondary-full { min-height: 44px; color: white; border: 1px solid transparent; border-radius: 10px; background: linear-gradient(135deg,#5378ef,#6967ee); font-weight: 800; }
        .soli-actions button.secondary, .soli-secondary-full { background: #151e2e; border-color: #2c3f65; }
        .soli-risk-hero { margin: 18px; padding: 22px; text-align: center; border-radius: 13px; background: #151e2e; border: 1px solid #293b5e; }
        .soli-risk-hero span { display: block; color: #9ba8be; font-size: 11px; text-transform: uppercase; letter-spacing: .08em; }
        .soli-risk-hero strong { display: block; margin: 8px 0; font-size: 34px; }
        .soli-risk-hero b { font-size: 13px; }
        .soli-risk-hero.extreme, .soli-risk-hero.high { border-color: rgba(239,127,143,.38); }
        .soli-risk-hero.medium { border-color: rgba(243,201,105,.32); }
        .soli-risk-hero.lower { border-color: rgba(89,211,155,.32); }
        .soli-check-list { display: grid; gap: 8px; padding: 0 18px; }
        .soli-check-list div { display: grid; grid-template-columns: 22px 1fr; gap: 8px; padding: 10px; color: #d6dded; background: #141c2b; border: 1px solid #25344f; border-radius: 9px; }
        .soli-check-list p { margin: 0; font-size: 12px; line-height: 1.45; }
        .soli-check-list span { color: #f3c969; }
        .soli-disclaimer { margin: 14px 18px; padding: 11px; color: #9da9bf; background: #0b111b; border-radius: 9px; font-size: 10px; line-height: 1.5; }
        .soli-primary-full, .soli-secondary-full { width: calc(100% - 36px); margin: 0 18px 18px; }
        .soli-finder-intro, .soli-paper-card, .soli-settings { display: grid; gap: 14px; padding: 18px; }
        .soli-finder-intro h2, .soli-paper-card h2 { margin: 0; color: #79a4ff; font-size: 18px; }
        .soli-finder-intro p, .soli-paper-card p { margin: 0; color: #b5bfd1; line-height: 1.55; font-size: 12px; }
        .soli-finder-intro .soli-primary-full, .soli-paper-card .soli-primary-full, .soli-paper-card .soli-secondary-full, .soli-settings .soli-secondary-full { width: 100%; margin: 0; }
        .soli-result-list { display: grid; gap: 7px; padding: 0 18px 18px; }
        .soli-result-list button { display: flex; justify-content: space-between; gap: 12px; padding: 11px; text-align: left; color: #f3f6ff; background: #141d2d; border: 1px solid #283853; border-radius: 10px; }
        .soli-result-list button:hover { border-color: #5074c7; }
        .soli-result-list button div { display: grid; gap: 4px; }
        .soli-result-list button div:last-child { justify-items: end; }
        .soli-result-list span { color: #8f9cb4; font-size: 10px; }
        .soli-paper-card > span { width: fit-content; padding: 5px 8px; color: #bff4d9; background: rgba(89,211,155,.12); border-radius: 999px; font-size: 10px; font-weight: 800; }
        .soli-inline-result { min-height: 18px; color: #aeb9ca; font-size: 11px; }
        .soli-portfolio-value { display: grid; justify-items: center; gap: 7px; margin: 18px; padding: 22px; background: linear-gradient(135deg,rgba(92,124,250,.13),rgba(84,200,232,.05)); border: 1px solid #30456e; border-radius: 13px; }
        .soli-portfolio-value strong { font-size: 30px; }
        .soli-portfolio-value small { color: #91a0ba; }
        .soli-section-title { margin: 6px 18px 10px; color: #79a4ff; font-size: 13px; }
        .soli-trades { display: grid; gap: 7px; padding: 0 18px 18px; }
        .soli-trades div { display: flex; justify-content: space-between; gap: 12px; padding: 10px; background: #141d2d; border: 1px solid #283853; border-radius: 9px; font-size: 11px; }
        .soli-trades span { color: #99a6ba; }
        .soli-settings output { float: right; color: #79a4ff; }
        .soli-settings input[type="range"] { min-height: auto; padding: 0; accent-color: #5c7cfa; border: 0; }
        .soli-toggle-row { position: relative; display: flex; justify-content: space-between; align-items: center; min-height: 38px; color: #c7d0e1; font-size: 12px; }
        .soli-toggle-row input { position: absolute; opacity: 0; }
        .soli-toggle-row i { position: relative; width: 44px; height: 24px; border-radius: 999px; background: #26334c; }
        .soli-toggle-row i::before { content: ""; position: absolute; left: 3px; top: 3px; width: 18px; height: 18px; border-radius: 50%; background: white; transition: .18s; }
        .soli-toggle-row input:checked + i { background: #4468bb; }
        .soli-toggle-row input:checked + i::before { transform: translateX(20px); }
        .soli-error { margin: 18px; padding: 16px; color: #ffd3d9; background: rgba(239,127,143,.08); border: 1px solid rgba(239,127,143,.25); border-radius: 10px; }
        .soli-error p { color: #c7b6be; line-height: 1.5; }
        .soli-error code { color: #f2d3dc; }
        :host-context(.soli-compact-host) .soli-panel { width: 360px; }
    '''),
    "extension/README.md": clean(r'''
        # SOLI AI Axiom Overlay

        This is a local-development Chrome/Edge/Brave extension for the SOLI AI project.

        ## Install

        1. Start the local backend from the project root:

           ```powershell
           python server.py
           ```

        2. Open `chrome://extensions`.
        3. Enable **Developer mode**.
        4. Choose **Load unpacked**.
        5. Select this `extension` folder.
        6. Open or refresh `https://axiom.trade/`.

        ## What the overlay uses

        - `GET /api/status`
        - `GET /api/check?symbol=<mint>`
        - `GET /api/find?...`
        - `GET /api/portfolio?symbol=<mint>`
        - `GET /api/buy?symbol=<mint>&units=<units>`
        - `GET /api/sell?symbol=<mint>`

        The last two routes are expected to be **paper-trading routes** in the current backend.

        ## Security boundaries

        - No wallet private key is requested.
        - No live swap is created.
        - The extension communicates with `http://127.0.0.1:5500`.
        - Do not add private keys to extension code or Chrome storage.
        - Replace state-changing GET endpoints with POST endpoints before any public release.
    '''),
    "SOLI_AI_BUILD_GUIDE.md": clean(r'''
        # SOLI AI Website + Axiom Overlay Build Guide

        ## What this generator creates

        Running `python build_soli_ai.py --apply` creates two connected frontend products:

        1. A public SOLI AI website and dashboard in `web_static/`.
        2. A Chrome/Edge/Brave Axiom overlay in `extension/`.

        Your existing `server.py` remains the backend and continues to provide `/api/...` routes.

        ## Step 1 — Back up the project

        Commit your current project to Git or copy it before running the generator. The generator also creates timestamped backups automatically when it replaces an existing `web_static` or `extension` directory.

        ## Step 2 — Run the generator

        In VS Code PowerShell:

        ```powershell
        cd "C:\path\to\your\SOLI-AI-project"
        python build_soli_ai.py --apply
        ```

        You should see a list of generated files.

        ## Step 3 — Confirm the backend dependencies

        Your existing backend needs its normal requirements:

        ```powershell
        py -m venv .venv
        Set-ExecutionPolicy -Scope Process Bypass
        .\.venv\Scripts\Activate.ps1
        python -m pip install --upgrade pip
        pip install -r requirements.txt
        ```

        ## Step 4 — Start SOLI AI

        ```powershell
        python server.py
        ```

        Then test these addresses:

        - `http://127.0.0.1:5500/api/status`
        - `http://127.0.0.1:5500/`
        - `http://127.0.0.1:5500/dashboard.html`
        - `http://127.0.0.1:5500/setup.html`

        ## Step 5 — Install the extension

        1. Open `chrome://extensions`.
        2. Enable **Developer mode**.
        3. Select **Load unpacked**.
        4. Choose the generated `extension` folder.
        5. Open or refresh Axiom.

        ## Step 6 — Test the overlay in order

        1. Open the extension popup and select **Check local backend**.
        2. Confirm the panel appears on Axiom.
        3. Drag the header and confirm its position is remembered.
        4. Collapse and reopen the panel.
        5. Paste a Solana mint manually.
        6. Open **AI Token Analysis**.
        7. Open **Rug Pull Detector**.
        8. Run **Token Finder**.
        9. Test a paper buy with a very small simulated unit amount.
        10. Restart the backend and confirm the extension displays a useful error rather than disappearing.

        ## Existing backend behavior expected by the frontend

        ### `/api/status`

        Returns backend identity and current default configuration.

        ### `/api/find`

        Expected response:

        ```json
        {
          "tokens": [
            {
              "name": "Example",
              "token_symbol": "EX",
              "mint": "...",
              "price_usd": 0.00003,
              "liquidity_usd": 50000,
              "volume_24h": 125000,
              "price_change_24h": 18.5,
              "rug_score": 32,
              "rug_flags": []
            }
          ]
        }
        ```

        ### `/api/check?symbol=<mint>`

        Expected fields include:

        - `assistant_summary`
        - `signal`
        - `rug_summary.score`
        - `rug_summary.flags`
        - `pair_info.priceUsd`
        - `pair_info.liquidity.usd`
        - `pair_info.volume.h24`
        - `pair_info.baseToken.name`
        - `pair_info.baseToken.symbol`

        ### Paper endpoints

        The generated frontend currently calls the routes already present in your backend:

        - `/api/buy?symbol=<mint>&units=<units>`
        - `/api/sell?symbol=<mint>`

        They must remain simulated. Before a public release, replace state-changing GET requests with authenticated POST requests and CSRF protections.

        ## Important data fixes still required

        The user interface cannot make incorrect backend data correct. Complete these backend tasks:

        1. Normalize risk scores to a documented 0–100 scale in Python.
        2. Use one pair-selection function for `/api/find`, `/api/check`, `/api/portfolio`, `/api/buy`, and `/api/sell`.
        3. Do not call exchange OHLCV logic for a Solana mint.
        4. Return pair age and buy/sell counts directly from the selected Solana pair.
        5. Cache discovery results for roughly 20–30 seconds.
        6. Cache holder/rug analysis for several minutes.
        7. Use `ThreadingHTTPServer` or a production web framework so slow risk checks do not block all requests.
        8. Store watchlists in SQLite if you want them to survive restarts.
        9. Add a snapshot table before showing historical price charts.

        ## Recommended next backend tables

        ```sql
        CREATE TABLE IF NOT EXISTS watchlist (
            mint TEXT PRIMARY KEY,
            name TEXT,
            symbol TEXT,
            added_at TEXT NOT NULL
        );

        CREATE TABLE IF NOT EXISTS token_snapshots (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            mint TEXT NOT NULL,
            timestamp TEXT NOT NULL,
            price_usd REAL,
            liquidity_usd REAL,
            market_cap_usd REAL,
            volume_h24 REAL
        );
        ```

        ## Development roadmap

        ### Milestone 1 — Reliable research data

        - One token snapshot function
        - Accurate liquidity and price
        - Pair age
        - Buy/sell counts
        - Documented risk scale
        - Server-side caching

        ### Milestone 2 — Product experience

        - Website landing page
        - Full dashboard
        - Axiom overlay
        - Persistent settings
        - Watchlist
        - Paper portfolio

        ### Milestone 3 — Better analysis

        - Mint and freeze authority
        - Holder concentration
        - Liquidity-to-market-cap ratio
        - Momentum warnings
        - Social links and website verification
        - Transparent explanation of missing data

        ### Milestone 4 — Historical data

        - Background snapshot collector
        - Price chart
        - Liquidity chart
        - Watchlist alerts
        - Paper-trade performance history

        ### Milestone 5 — Public deployment

        - Move from the development HTTP server to a maintained framework
        - Authentication and user accounts
        - Rate limiting
        - HTTPS
        - Database migrations
        - Privacy policy and terms
        - Monitoring and error reporting
        - No private keys in browser code

        ### Milestone 6 — Live execution, only after independent review

        Live trading should be a separate, audited backend service with strict risk limits, burner-wallet requirements, transaction previews, exact confirmation, and an emergency disable switch. Do not place signing secrets in the website or extension.

        ## Common problems

        ### The landing page opens but the dashboard shows no tokens

        Open `/api/find?limit=12`. If it returns an empty `tokens` array, the issue is in the discovery backend rather than the frontend.

        ### The overlay says the backend is unavailable

        Confirm `python server.py` is still running and that `/api/status` works in the browser.

        ### No token is detected on Axiom

        Axiom may change its URLs or page markup. Paste the mint manually. Then update `detectMint()` in `extension/content.js` once you identify a reliable page source.

        ### Changes to extension files do not appear

        Return to `chrome://extensions`, press the extension reload button, and refresh the Axiom tab.

        ### The extension appears under Axiom elements

        The generated host uses a high z-index. If Axiom introduces a higher one, raise the z-index on `#soli-ai-overlay-host` by adding a host style in `content.js` or wrapping the panel in a fixed-position element.
    '''),
}


def backup(path: Path) -> Path | None:
    if not path.exists():
        return None
    stamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_root = ROOT / "backups"
    backup_root.mkdir(exist_ok=True)
    destination = backup_root / f"{path.name}_{stamp}"
    if path.is_dir():
        shutil.copytree(path, destination)
    else:
        shutil.copy2(path, destination)
    return destination


def write_files(force: bool) -> None:
    if force:
        for dirname in ("web_static", "extension"):
            target = ROOT / dirname
            if target.exists():
                destination = backup(target)
                print(f"Backed up {target.name} -> {destination}")
                shutil.rmtree(target)

    skipped: list[str] = []
    written: list[str] = []
    for relative, content in FILES.items():
        target = ROOT / relative
        target.parent.mkdir(parents=True, exist_ok=True)
        if target.exists() and not force:
            skipped.append(relative)
            continue
        target.write_text(content, encoding="utf-8")
        written.append(relative)

    print("\nGenerated files:")
    for item in written:
        print(f"  + {item}")
    if skipped:
        print("\nSkipped existing files (run with --apply to back up and replace web_static/extension):")
        for item in skipped:
            print(f"  - {item}")

    print("\nNext steps:")
    print("  1. Run: python server.py")
    print("  2. Open: http://127.0.0.1:5500/")
    print("  3. Open: http://127.0.0.1:5500/dashboard.html")
    print("  4. Load the extension folder from chrome://extensions")
    print("  5. Read SOLI_AI_BUILD_GUIDE.md")


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate the SOLI AI website and Axiom overlay extension.")
    parser.add_argument(
        "--apply",
        action="store_true",
        help="Back up and replace existing web_static and extension directories.",
    )
    parser.add_argument(
        "--preview",
        action="store_true",
        help="List files that would be created without writing them.",
    )
    args = parser.parse_args()

    if args.preview:
        print("SOLI AI generator would create:")
        for relative in FILES:
            print(f"  - {relative}")
        return

    write_files(force=args.apply)


if __name__ == "__main__":
    main()
