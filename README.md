# 🚗 Vehicle Survey using Object Detection (YOLOv11)

This project demonstrates a **Vehicle Survey System** that uses **YOLOv11** (You Only Look Once) — a state-of-the-art object detection model — to detect and count vehicles in real-time from video footage or live camera streams.  
It helps analyze **traffic flow**, **vehicle density**, and can be applied for **intelligent transportation systems** or **smart city analytics**.

---

## 🧠 Features

- 🚘 **Real-time vehicle detection** using YOLOv11  
- 📊 **Automatic vehicle counting** for traffic survey and monitoring  
- 🎥 **Video input support** — works with both recorded and live CCTV feeds  
- 💾 **Frame-by-frame analysis** with visualization overlays  
- 📈 **Statistics and insights** for vehicle flow and congestion estimation  

---

## 🛠️ Technologies Used

- **Python 3.10+**  
- **YOLOv11** (Ultralytics)  
- **OpenCV** — for image/video processing  
- **NumPy** — for numerical operations  
- **Matplotlib / CSV** — for visualization and data export  

NOTE:This python script uses the ultralytics version==8.3.5



---

## ⚙️ Installation

Install libraries.

--> pip install opencv-python
--> pip install ultralytics==8.3.5

Clone the repository:

```bash
git clone https://github.com/rajasekaran12345/Vechicle-Survey-using-object-detection-YOLOV11l.git
cd Vechicle-Survey-using-object-detection-YOLOV11l
``

---

## ▶️ Usage

1. Place your **input video** in the project folder.  
2. Run the main script:

```bash
python vehicle_survey.py
```

3. The system will:
   - Detect vehicles using YOLOv11  
   - Draw bounding boxes on each detected vehicle  
   - Count the number of vehicles passing through defined regions  
   - Display the live output with vehicle count  

---

## 📊 Output

- **Real-time annotated video** with bounding boxes and vehicle counts  
- **CSV file** storing vehicle statistics (optional)  
- **Graphical summary** (if enabled) for traffic trend analysis  

---

## 📚 Learnings

Through this project, I learned:
- Integrating **YOLOv11l** for real-world object detection tasks  
- Using **OpenCV** for real-time image processing  
- Implementing **region-based counting** for traffic analytics  
- Building a simple, yet effective **vehicle survey system**  

---

## 🚀 Future Enhancements

- Classification by vehicle type (car, bus, bike, truck)  
- Integration with a **dashboard** for real-time analytics  
- Support for **cloud-based video streaming**  
- Deployment using **Flask** or **Streamlit** for live demos  

---

## 🙌 Acknowledgements

- **Ultralytics** for the YOLOv11 model  
- **OpenCV Community** for vision tools  
- Inspiration from real-world **traffic monitoring systems**  

---

## 📧 Contact

👤 **Rajasekaran M**  
📍 Data Science & AI Enthusiast | Machine Learning Developer  
🔗 [LinkedIn](https://www.linkedin.com/in/rajasekaran-m-492808224/)  
💻 [GitHub](https://github.com/rajasekaran12345)
