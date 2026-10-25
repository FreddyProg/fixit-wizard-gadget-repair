# FIXIT WIZARD

FIXIT WIZARD is a responsive landing page for a smartphone and gadget repair service. It presents repair services, a promotional video, the company story, and a client-side repair estimate form.

## Features

- Responsive navigation with a mobile menu
- Hero section with repair-service messaging and calls to action
- Service cards for:
  - Screen repair
  - Battery and charging support
  - Software support
- Promotional video with a custom poster image
- Company story and service promise sections
- Repair estimate form with client-side status feedback
- Smooth scrolling and responsive styling

## Project structure

```text
.
├── index.html          # Main landing page
├── styles.css          # Layout, responsive styles, and visual design
├── main.py             # PyScript form and navigation interactions
├── advertisement.mp4   # Promotional video
└── video-poster.svg    # Video fallback poster image
```

## Running locally

This is a static website, but `main.py` is loaded through [PyScript](https://pyscript.net/) and the page imports external assets from the web. Serve the project through a local HTTP server rather than opening `index.html` directly.

### Option 1: Python

From the project directory, run:

```bash
python -m http.server 8000
```

Then open <http://localhost:8000> in a modern web browser.

### Option 2: VS Code Live Server

1. Install the **Live Server** extension.
2. Open the project folder in VS Code.
3. Right-click `index.html`.
4. Select **Open with Live Server**.

## Notes

- An internet connection is needed to load the PyScript runtime and Google Fonts.
- The estimate form is currently client-side only. It displays a confirmation message but does not send data to a backend.
- Replace `advertisement.mp4` with an updated video file if the promotional content changes.
