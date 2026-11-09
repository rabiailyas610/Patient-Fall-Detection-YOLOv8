# Privacy-Preserving Patient Fall Detection & Behavior Monitoring Dashboard

An academic-grade, real-time edge computer vision framework developed using **YOLOv8-Pose** and **OpenCV** to automate patient fall detection in smart healthcare environments without compromising identity privacy.

## 🚀 Key Features
- **Parallel Edge Inference:** Real-time human skeletal topology extraction using localized YOLOv8 configurations.
- **Custom Spatial Heuristics:** Implemented vertical orientation tracking via Nose-to-Hip Centroid displacement vectors (`V-DISPLACE`).
- **Telemetry HUD Dashboard:** Live tracking metrics showing Frames Per Second (`EDGE SPEED`), spatial distance in pixels, and critical incident logs (`ALARM LOGS`).
- **Dynamic Anomaly Alerting:** Alpha-blended crimson overlay flash system triggered instantly on spatial threshold collapse (<60px).

## 📊 Telemetry System Architecture

| Parameter | Technical Definition | Academic Value |
| :--- | :--- | :--- |
| **EDGE SPEED (FPS)** | Latency measurement per frame matrix processing. | Evaluates model optimization for resource-constrained Edge devices. |
| **V-DISPLACE (px)** | Vertical Euclidean displacement between Nose and Hip Centroid. | Core mathematical heuristic used to eliminate false positives in bounding boxes. |
| **ALARM LOGS** | Continuous tracking arrays logging frame anomaly confirmations. | Essential data metrics for automated hospital notification logging systems. |

## 🛠️ Installation & Execution

### 1. Requirements
Ensure you install the required packages through your terminal:
```bash
pip install ultralytics opencv-python numpy
```

### 2. Running the System
Execute the primary framework terminal node:
```bash
python "Patient fall.py"
```

## 🔬 Mathematical Logic & Research Approach
Instead of relying on heavy bounding-box overlaps that frequently cause false positives during casual sitting or bending, this framework monitors the precise bipedal spatial vector collapse. Whenever the vertical displacement between the nose and the computed hip centroid breaches the baseline critical threshold of **60 pixels** on a 480p continuous matrix stream, an automated horizontal axis collapse anomaly is flagged.
