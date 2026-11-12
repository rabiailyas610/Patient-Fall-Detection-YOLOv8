import cv2
import numpy as np
import time
from ultralytics import YOLO

# =====================================================================
# 1. INITIALIZE INDUSTRIAL FRAMEWORK
# =====================================================================
model = YOLO("yolov8n-pose.pt")
cap = cv2.VideoCapture(0)  # Live Webcam

# Performance Metrics Variables
p_time = 0
fall_counter = 0

print("🔥 Advanced Healthcare Edge Monitor Active... Press 'q' to stop.")

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Matrix standard resizing
    frame = cv2.resize(frame, (854, 480)) # Widescreen dashboard format
    h, w, _ = frame.shape
    overlay = frame.copy() # For alpha-blending transparency effect

    # Calculate FPS (Processing Speed)
    c_time = time.time()
    fps = int(1 / (c_time - p_time))
    p_time = c_time

    # Run AI inference
    results = model(frame, verbose=False)
    
    # Baseline System States
    alert_status = "SYSTEM STATE: NOMINAL (PATIENT ACTIVE)"
    alert_color = (0, 255, 0)  # Cyber Green
    is_fall = False
    spatial_distance = 100  # Default dummy metric

    for r in results:
        if r.keypoints is not None and len(r.keypoints.xy) > 0:
            kp = r.keypoints.xy.cpu().numpy()
            
            for person in kp:
                if len(person) > 12:  
                    # Extract vital vectors (0=Nose, 11=L-Hip, 12=R-Hip)
                    nose_y = person[0][1]
                    left_hip_y = person[11][1]
                    right_hip_y = person[12][1]
                    
                    # Compute hip centroid vector
                    hip_center_y = (left_hip_y + right_hip_y) / 2
                    
                    # Heuristic orientation math
                    spatial_distance = abs(nose_y - hip_center_y)
                    
                    # Emergency Trigger Threshold
                    if spatial_distance < 60 and nose_y > 0:
                        is_fall = True
                        fall_counter += 1
                        alert_status = "⚠️ ANOMALY: PATIENT CRITICAL FALL DETECTED!"
                        alert_color = (0, 0, 255)  # Crimson Red
                        
                    # Auto render skeletal nodes on overlay mesh
                    frame = r.plot(boxes=False, labels=False)

    # =====================================================================
    # 2. ADVANCED CYBERPUNK INTERFACE DESIGN (ENTERPRISE UI)
    # =====================================================================
    if is_fall:
        # 🚨 ADVANCED FEATURE 1: Red screen flash overlay on boundary collapse
        cv2.rectangle(overlay, (0, 0), (w, h), (0, 0, 255), -1)
        cv2.addWeighted(overlay, 0.25, frame, 0.75, 0, frame)
        # Windows native sound system trigger can be un-commented if needed:
        # import winsound; winsound.Beep(1000, 200)

    # Top Control Banner (Semi-transparent black overlay)
    cv2.rectangle(overlay, (0, 0), (w, 75), (15, 15, 15), -1)
    cv2.addWeighted(overlay, 0.4, frame, 0.6, 0, frame)
    
    # Status Render
    cv2.putText(frame, alert_status, (20, 48), cv2.FONT_HERSHEY_DUPLEX, 0.8, alert_color, 2)

    # 📊 ADVANCED FEATURE 2: Real-time Metrics Sidebar (HUD Display)
    # Background Sidebar
    cv2.rectangle(frame, (w - 240, 90), (w - 15, 230), (30, 30, 30), -1)
    cv2.rectangle(frame, (w - 240, 90), (w - 15, 230), (100, 100, 100), 1)
    
    # Live HUD Metrics text
    cv2.putText(frame, f"EDGE SPEED: {fps} FPS", (w - 225, 125), cv2.FONT_HERSHEY_SIMPLEX, 0.55, (255, 255, 255), 1)
    cv2.putText(frame, f"V-DISPLACE: {int(spatial_distance)}px", (w - 225, 160), cv2.FONT_HERSHEY_SIMPLEX, 0.55, (0, 255, 255), 1)
    cv2.putText(frame, f"ALARM LOGS: {fall_counter}", (w - 225, 195), cv2.FONT_HERSHEY_SIMPLEX, 0.55, (0, 165, 255), 1)

    # Dashboard Tech Watermarks
    cv2.putText(frame, "LAB ENGINE v2.4 || CORE: COMPUTE_EDGE_X86", (20, h - 20), 
                cv2.FONT_HERSHEY_SIMPLEX, 0.4, (120, 120, 120), 1)

    # Render complete advanced window
    cv2.imshow("Academic Fall Detection & Orientation Analysis System", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
print("📊 Processing successfully finalized.")
