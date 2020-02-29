import cv2
import numpy as np


with open("yolov3.txt", 'r') as f:
        classes = [line.strip() for line in f.readlines()]
colors = np.random.uniform(0, 300, size=(len(classes), 3))
net = cv2.dnn.readNet("yolov3.weights", "yolov3.cfg")
cap = cv2.VideoCapture(0)
scale = 0.00392
conf_threshold = 0.5
nms_threshold = 0.4

def get_output_layers(net):
    layer_names = net.getLayerNames()
    output_layers = [layer_names[i[0] - 1] for i in net.getUnconnectedOutLayers()]
    return output_layers



def create_bounding_boxes(outs,Width, Height):
    boxes = []
    class_ids = []
    confidences = []
    for out in outs:
        for detection in out:
            scores = detection[5:]
            class_id = np.argmax(scores)
            confidence = scores[class_id]
            if confidence > conf_threshold:
                center_x = int(detection[0] * Width)
                center_y = int(detection[1] * Height)
                w = int(detection[2] * Width)
                h = int(detection[3] * Height)
                x = center_x - w / 2
                y = center_y - h / 2
                class_ids.append(class_id)
                confidences.append(float(confidence))
                boxes.append([x, y, w, h])
    return boxes, class_ids, confidences

def draw_bounding_boxes(img, class_id, confidence, box):
    
    x = round(box[0])
    y = round(box[1])
    w = round(box[2])
    h =round(box[3])
    x_plus_w = x+w
    y_plus_h = y+h
    label = str(classes[class_id])
    color = colors[class_id]
    cv2.rectangle(img, (x,y), (x_plus_w,y_plus_h), color, 2)
    cv2.putText(img, label, (x-10,y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)

def Yolo(image):
    try:
        Width = image.shape[1]
        Height = image.shape[0]
        blob = cv2.dnn.blobFromImage(image, scale, (416,416), (0,0,0), True, crop=False)
        net.setInput(blob)
        outs = net.forward(get_output_layers(net))
        boxes, class_ids, confidences = create_bounding_boxes(outs, Width, Height)
        indices = cv2.dnn.NMSBoxes(boxes, confidences, conf_threshold, nms_threshold)

        for i in indices:
            i = i[0]
            box = boxes[i]
            
            draw_bounding_boxes(image, class_ids[i], confidences[i], box)
    except Exception as e:
        print('Failed dnn: '+ str(e))
    
    return image

while True:
    ret, frame = cap.read()
    image = Yolo(frame)
    cv2.imshow('frame',image)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()