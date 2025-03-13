import sys
import yolov9.models
import yolov9.models.yolo

sys.modules["models"] = yolov9.models
sys.modules["models.yolo"] = yolov9.models.yolo
