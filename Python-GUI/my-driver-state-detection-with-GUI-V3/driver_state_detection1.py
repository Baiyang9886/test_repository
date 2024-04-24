import math
import time
import cv2
import mediapipe as mp
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


class Face_mesh():
    def __init__(self):
        super(Face_mesh, self).__init__()
        self.mp_face_mesh = mp.solutions.face_mesh
        self.start_time = time.time()
        self.face_mesh = self.mp_face_mesh.FaceMesh(static_image_mode=True, max_num_faces=3,
                                               refine_landmarks=True, min_detection_confidence=0.5, min_tracking_confidence=0.5)
        self.mp_drawing = mp.solutions.drawing_utils
        self.mp_drawing_styles = mp.solutions.drawing_styles

        self.frame = np.zeros([640, 480], dtype='uint8')
        self.annotated_image = np.zeros([640, 480], dtype='uint8')
        self.left_eye_image = np.zeros([640, 480], dtype='uint8')
        self.right_eye_image = np.zeros([640, 480], dtype='uint8')
        self.mouth_image = np.zeros([640, 480], dtype='uint8')
        self.yawn_time = [-1]
        self.yawn_duration = 0
        self.yawn_interval = [1]
        self.yawn_frequency = []
        self.start_blink_time = [-1]
        self.blink_duration = 0
        self.blink_interval = [1]
        self.blink_frequency = []

        self.angle_yaw = [0]
        self.angle_pitch = [0]
        self.angle_roll = [0]
        self.gaze_yaw = [0]
        self.gaze_pitch = [0]
        self.gaze_roll = [0]
        self.eye_close = False
        self.yawning = False

        self.right_iris = [474, 475, 476, 477, 474]
        self.left_iris = [469, 470, 471, 472, 469]
        self.right_eye = [263, 466, 388, 387, 386, 385, 384, 398, 362, 382, 381, 380, 374, 373, 390, 249, 263]
        self.left_eye = [7, 33, 246, 161, 160, 159, 158, 157, 173, 133, 155, 154, 153, 145, 144, 163, 7]
        self.right_eyebrow = [336, 296, 334, 293, 300, 276, 283, 282, 295, 285, 336]
        self.left_eyebrow = [55, 65, 52, 53, 46, 70, 63, 105, 66, 107, 55]
        self.contours_face = [356, 454, 323, 361, 288, 397, 365, 379, 378, 400, 377, 152, 148, 176, 149, 150, 136, 172, 58, 132, 93,
                              234, 127, 162, 21, 54, 103, 67, 109, 10, 338, 297, 332, 284, 251, 389, 356]
        self.mouth_inner = [78, 191, 80, 81, 82, 13, 312, 311, 310, 415, 308, 324, 318, 402, 317, 14, 87, 178, 88, 95, 78]
        self.mouth_outer = [61, 185, 40, 39, 37, 0, 267, 269, 270, 409, 291, 375, 321, 405, 314, 17, 84, 181, 91, 146, 61]

    def head_pose_calculation(self, landmarks, landmark, points, frame_shape):
        '''
            yaw is calculate according to landmark point 10 and 164
           pitch is calculate according to landmark point 132 and 361
           roll is calculate according to point 94 and the middle point of 132 and 361
        '''

        coord_len = 0.1
        head_pose_angle_num = 20
        p10 = landmarks[10]
        p4 = landmarks[94]
        p152 = landmarks[164]
        p132 = landmarks[132]
        p361 = landmarks[361]
        pm = [(p132.x + p361.x)/2, (p132.y + p361.y)/2, (p132.z + p361.z)/2]
        coord = [p4.x, p4.y, p4.z]
        annotated_image = np.zeros(frame_shape, dtype='uint8')
        h, w = frame_shape[:-1]

        contour_pts = []
        for c in self.contours_face:
            contour_pts.append(points[c])
        contour_pts = np.array(contour_pts)
        cv2.polylines(annotated_image, [contour_pts], False, (255, 255, 255), thickness=2)

        self.mp_drawing.draw_landmarks(image=annotated_image, landmark_list=landmark,
                                       connections=self.mp_face_mesh.FACEMESH_TESSELATION,  ### 绘制网格
                                       landmark_drawing_spec=None,
                                       connection_drawing_spec=self.mp_drawing_styles.get_default_face_mesh_tesselation_style())

        # coord = pm
        disyaw = np.sqrt(np.square(p10.x - p152.x) + np.square(p10.y - p152.y) + np.square(p10.z - p152.z))
        dispitch = np.sqrt(np.square(p132.x - p361.x) + np.square(p132.y - p361.y) + np.square(p132.z - p361.z))
        disroll = np.sqrt(np.square(pm[0] - p4.x) + np.square(pm[1] - p4.y) + np.square(pm[2] - p4.z))

        vecyaw = [(p152.x - p10.x)/disyaw, (p152.y - p10.y)/disyaw, (p152.z - p10.z)/disyaw]
        vecpitch = [(p361.x - p132.x)/dispitch, (p361.y - p132.y)/dispitch, (p361.z - p132.z)/dispitch]
        vecroll = [(p4.x - pm[0])/disroll, (p4.y - pm[1])/disroll, (p4.z - pm[2])/disroll]

        yaw = [coord[0] + vecyaw[0] * coord_len, coord[1] + vecyaw[1] * coord_len, coord[2] + vecyaw[2] * coord_len]
        pitch = [coord[0] + vecpitch[0] * coord_len, coord[1] + vecpitch[1] * coord_len, coord[2] + vecpitch[2] * coord_len]
        roll = [coord[0] + vecroll[0] * coord_len, coord[1] + vecroll[1] * coord_len, coord[2] + vecroll[2] * coord_len]

        cv2.arrowedLine(annotated_image, (int(coord[0] * w), int(coord[1] * h)), (int(yaw[0] * w), int(yaw[1] * h)),
                        (255, 0, 0), 3)   # the blue axis
        cv2.arrowedLine(annotated_image, (int(coord[0] * w), int(coord[1] * h)), (int(pitch[0] * w), int(pitch[1] * h)),
                        (0, 255, 0), 3)   # the green axis
        cv2.arrowedLine(annotated_image, (int(coord[0] * w), int(coord[1] * h)), (int(roll[0] * w), int(roll[1] * h)),
                        (0, 0, 255), 3)   # the red axis

        angle_yaw = (roll[0] * w - coord[0] * w) * 1.6
        angle_pitch = (roll[1] * h - coord[1] * h) * 2
        angle_roll = math.atan((pitch[1] * h - coord[1] * h) / (pitch[0] * w - coord[0] * w)) * 90

        self.angle_yaw.append(angle_yaw)
        self.angle_pitch.append(angle_pitch)
        self.angle_roll.append(angle_roll)

        if len(self.angle_yaw) > head_pose_angle_num:
            self.angle_yaw.pop(0)
        if len(self.angle_pitch) > head_pose_angle_num:
            self.angle_pitch.pop(0)
        if len(self.angle_roll) > head_pose_angle_num:
            self.angle_roll.pop(0)

        # print("yaw_blue:" + str(angle_yaw))
        # print("pitch_green:" + str(angle_pitch))
        # print("roll_red:" + str(angle_roll))

        return vecroll, annotated_image


    def gaze_direction_calculation(self, vector, landmarks, frame_shape):
        iris_r = -0.012
        arrow_len = 0.1
        gaze_angle_num = 10
        h, w = frame_shape[:-1]

        ave_left_x, ave_left_y, ave_left_z = 0, 0, 0
        for k in self.left_eye:
            eye_point = landmarks[k]
            ave_left_x = ave_left_x + eye_point.x
            ave_left_y = ave_left_y + eye_point.y
            ave_left_z = ave_left_z + eye_point.z
        ave_left_x = ave_left_x / len(self.left_eye)
        ave_left_y = ave_left_y / len(self.left_eye)
        ave_left_z = ave_left_z / len(self.left_eye)
        left_eye_center = [ave_left_x + vector[0]*iris_r, ave_left_y + vector[1]*iris_r, ave_left_z + vector[2]*iris_r]

        ave_right_x, ave_right_y, ave_right_z = 0, 0, 0
        for k in self.right_eye:
            eye_point = landmarks[k]
            ave_right_x = ave_right_x + eye_point.x
            ave_right_y = ave_right_y + eye_point.y
            ave_right_z = ave_right_z + eye_point.z
        ave_right_x = ave_right_x / len(self.right_eye)
        ave_right_y = ave_right_y / len(self.right_eye)
        ave_right_z = ave_right_z / len(self.right_eye)
        right_eye_center = [ave_right_x + vector[0] * iris_r, ave_right_y + vector[1] * iris_r,
                           ave_right_z + vector[2] * iris_r]

        iris_left_x, iris_left_y, iris_left_z = 0, 0, 0
        for k in self.left_iris:
            iris_point = landmarks[k]
            iris_left_x = iris_left_x + iris_point.x
            iris_left_y = iris_left_y + iris_point.y
            iris_left_z = iris_left_z + iris_point.z
        iris_left_p = [iris_left_x / len(self.left_iris), iris_left_y / len(self.left_iris), iris_left_z / len(self.left_iris)]

        iris_right_x, iris_right_y, iris_right_z = 0, 0, 0
        for k in self.right_iris:
            iris_point = landmarks[k]
            iris_right_x = iris_right_x + iris_point.x
            iris_right_y = iris_right_y + iris_point.y
            iris_right_z = iris_right_z + iris_point.z
        iris_right_p = [iris_right_x / len(self.right_iris), iris_right_y / len(self.right_iris), iris_right_z / len(self.right_iris)]

        left_dis = np.sqrt(np.square(iris_left_p[0] - left_eye_center[0]) + np.square(iris_left_p[1] - left_eye_center[1])
                           + np.square(iris_left_p[2] - left_eye_center[2]))
        left_vector = [(iris_left_p[0] - left_eye_center[0])/left_dis, (iris_left_p[1] - left_eye_center[1])/left_dis,
                       (iris_left_p[2] - left_eye_center[2])/left_dis]

        right_dis = np.sqrt(np.square(iris_right_p[0] - right_eye_center[0]) + np.square(iris_right_p[1] - right_eye_center[1])
                           + np.square(iris_right_p[2] - right_eye_center[2]))
        right_vector = [(iris_right_p[0] - right_eye_center[0]) / right_dis,
                       (iris_right_p[1] - right_eye_center[1]) / right_dis,
                       (iris_right_p[2] - right_eye_center[2]) / right_dis]
        vector = [(left_vector[0] + right_vector[0])/2, (left_vector[1] + right_vector[1])/2, (left_vector[2] + right_vector[2])/2, ]

        # left_end = [left_eye_center[0] + left_vector[0] * arrow_len, left_eye_center[1] + left_vector[1] * arrow_len,
        #             left_eye_center[2] + left_vector[2] * arrow_len]
        # right_end = [right_eye_center[0] + right_vector[0] * arrow_len, right_eye_center[1] + right_vector[1] * arrow_len,
        #             right_eye_center[2] + right_vector[2] * arrow_len]
        left_end = [left_eye_center[0] + vector[0] * arrow_len, left_eye_center[1] + vector[1] * arrow_len,
                    left_eye_center[2] + vector[2] * arrow_len]
        right_end = [right_eye_center[0] + vector[0] * arrow_len,
                     right_eye_center[1] + vector[1] * arrow_len,
                     right_eye_center[2] + vector[2] * arrow_len]

        v_w = vector[0] * w
        v_h = vector[1] * h
        v_l = vector[2] * 500
        gaze_yaw = -math.atan(v_w / v_l) * 72
        gaze_pitch = -math.atan(v_h / v_l) * 72
        self.gaze_yaw.append(gaze_yaw)
        self.gaze_pitch.append(gaze_pitch)

        if len(self.gaze_yaw) > gaze_angle_num:
            self.gaze_yaw.pop(0)
        if len(self.gaze_pitch) > gaze_angle_num:
            self.gaze_pitch.pop(0)

        return left_eye_center, left_end, right_eye_center, right_end


    def show_eyes(self, points, frame_shape):
        record_time = 4
        b_rate = 0.13
        blink_rate = 0.18
        left_image = np.zeros(frame_shape, dtype='uint8')
        right_image = np.zeros(frame_shape, dtype='uint8')
        leye_left = points[33]
        leye_right = points[133]
        leye_top = points[159]
        leye_bottom = points[145]
        reye_left = points[362]
        reye_right = points[263]
        reye_top = points[386]
        reye_bottom = points[374]
        leye_w = np.sqrt(np.square(leye_left[0]-leye_right[0]) + np.square(leye_left[1] - leye_right[1]))
        leye_h = np.sqrt(np.square(leye_bottom[0] - leye_top[0]) + np.square(leye_bottom[1] - leye_top[1]))
        reye_w = np.sqrt(np.square(reye_left[0] - reye_right[0]) + np.square(reye_left[1] - reye_right[1]))
        reye_h = np.sqrt(np.square(reye_bottom[0] - reye_top[0]) + np.square(reye_bottom[1] - reye_top[1]))

        if leye_h/leye_w < blink_rate or reye_h/reye_w < blink_rate:
            interval = time.time() - self.start_blink_time[-1]
            self.eye_close = True
            if interval > 0.1:
                self.start_blink_time = []
                self.start_blink_time.append(time.time())
                self.blink_frequency.append(time.time())
            else:
                self.start_blink_time.append(time.time())
                self.blink_duration = (time.time() - self.start_blink_time[0]) * 100
        else:
            if time.time() - self.start_blink_time[-1] > 0.8:
                self.blink_duration = 0
                self.eye_close = False

        blink_interval = time.time() - self.start_blink_time[-1]
        self.blink_interval.append(blink_interval)
        if len(self.blink_interval) > 50:
            self.blink_interval.pop(0)
        if len(self.blink_frequency) > 0:
            inter = time.time() - self.blink_frequency[0]
            # print(inter)
            if inter > record_time:
                self.blink_frequency.pop(0)
        # print(len(self.blink_frequency))

        left_eye_pts = []
        letf_eyebrow = []
        left_iris = []
        right_eye_pts = []
        right_eyebrow = []
        right_iris = []

        for i in self.left_eye:
            left_eye_pts.append(points[i])

        for i in self.left_eyebrow:
            letf_eyebrow.append(points[i])

        for i in self.left_iris:
            left_iris.append(points[i])

        for i in self.right_eye:
            right_eye_pts.append(points[i])

        for i in self.right_eyebrow:
            right_eyebrow.append(points[i])

        for i in self.right_iris:
            right_iris.append(points[i])

        left_land_pts = np.array(left_eye_pts)
        left_x, left_y, left_w, left_h = cv2.boundingRect(left_land_pts)
        right_land_pts = np.array(right_eye_pts)
        right_x, right_y, right_w, right_h = cv2.boundingRect(right_land_pts)

        left_eye_pts = np.array(left_eye_pts)
        letf_eyebrow = np.array(letf_eyebrow)
        left_iris = np.array(left_iris)
        right_eye_pts = np.array(right_eye_pts)
        right_eyebrow = np.array(right_eyebrow)
        right_iris = np.array(right_iris)

        cv2.polylines(left_image, [left_eye_pts], False, (0, 255, 0), thickness=1)
        cv2.polylines(left_image, [left_iris], False, (255, 255, 255), thickness=1)
        cv2.polylines(right_image, [right_eye_pts], False, (0, 255, 0), thickness=1)
        cv2.polylines(right_image, [right_iris], False, (255, 255, 255), thickness=1)

        m_h, m_w = 50, 80
        left_eye = left_image[int(left_y - b_rate * left_h):int(left_y + (1 + b_rate) * left_h),
                              int(left_x - b_rate * left_w):int(left_x + (1 + b_rate) * left_w)]
        h, w = left_eye.shape[:-1]
        top = buttom = int((m_h - h) / 2)
        left = right = int((m_w - w) / 2)
        left_eye = cv2.copyMakeBorder(left_eye, top, buttom, left, right, cv2.BORDER_CONSTANT, None,
                                   (0, 0, 0))

        right_eye = right_image[int(right_y - b_rate * right_h):int(right_y + (1 + b_rate) * right_h),
                   int(right_x - b_rate * right_w):int(right_x + (1 + b_rate) * right_w)]
        h, w = right_eye.shape[:-1]
        top = buttom = int((m_h - h) / 2)
        left = right = int((m_w - w) / 2)
        right_eye = cv2.copyMakeBorder(right_eye, top, buttom, left, right, cv2.BORDER_CONSTANT, None,
                                   (0, 0, 0))

        # cv2.imshow("img_comb", left_eye)
        # cv2.waitKey(30)
        self.left_eye_image = left_eye
        self.right_eye_image = right_eye



    def get_order_of_facial_landmark_points(self, frame, landmark):
        h, w = frame.shape[:-1]
        contours = set(self.mp_face_mesh.FACEMESH_CONTOURS)
        contours_pp = []
        for x in contours:
            contours_pp.append(x[0])
            contours_pp.append(x[1])
        contours_set = set(contours_pp)
        left_eye = set(self.left_eye)
        left_eyebrow = set(self.left_eyebrow)
        right_eye = set(self.right_eye)
        right_eyebrow = set(self.right_eyebrow)
        face_oval = set(self.contours_face)
        mouth = contours_set - left_eyebrow - left_eye - right_eyebrow - right_eye - face_oval

        # show all facial landmark points with their index
        font = cv2.FONT_HERSHEY_SIMPLEX
        for con in mouth:
            if con < 50:
                print(con)
                contours_point = landmark[con]
                cv2.circle(frame, (int(contours_point.x * w), int(contours_point.y * h)), 2, (255, 255, 0), -1)
                cv2.putText(frame, str(con), (int(contours_point.x * w) + 2, int(contours_point.y * h) + 2), font,
                            0.2, (0, 255, 0), 1)

        mouth_pts = []
        # mouth = list(mouth)
        mouth_pts.append(14)
        connect_p = 14
        for i in range(10):
            print(connect_p)
            for p in contours:
                if p[1] == connect_p:
                    mouth_pts.append(p[0])
                    connect_p = p[0]
                    break
        print(mouth_pts)


    def show_mouth(self, points, frame_shape):
        record_time = 5
        b_rate = 0.13
        yawn_rate = 0.6
        mouth_image = np.zeros(frame_shape, dtype='uint8')
        mouth_inner_pts = []
        mouth_outer_pts = []
        m_top = points[13]
        m_bottom = points[14]
        m_left = points[78]
        m_right = points[308]
        mouth_h = np.sqrt(np.square(m_top[0] - m_bottom[0]) + np.square(m_top[1] - m_bottom[1]))
        mouth_w = np.sqrt(np.square(m_right[0] - m_left[0]) + np.square(m_right[1] - m_left[1]))

        if mouth_h/mouth_w > yawn_rate:
            self.yawning = True
            interval = time.time() - self.yawn_time[-1]
            self.yawn_interval.append(interval)
            if interval > 0.1:
                self.yawn_time = []
                self.yawn_time.append(time.time())
                self.yawn_frequency.append(time.time())
            else:
                self.yawn_time.append(time.time())
                self.yawn_duration = (time.time() - self.yawn_time[0]) * 100
        else:
            self.yawn_interval.append(1)
            if time.time() - self.yawn_time[-1] > 0.3:
                self.yawn_duration = 0
                self.yawning = False

        if len(self.yawn_interval) > 50:
            self.yawn_interval.pop(0)
        if len(self.yawn_frequency) > 0:
            inter = time.time() - self.yawn_frequency[0]
            if inter > record_time:
                self.yawn_frequency.pop(0)

        for i in self.mouth_inner:
            mouth_inner_pts.append(points[i])

        for i in self.mouth_outer:
            mouth_outer_pts.append(points[i])

        mouth_outer_pts = np.array(mouth_outer_pts)
        mouth_inner_pts = np.array(mouth_inner_pts)
        x, y, w, h = cv2.boundingRect(mouth_outer_pts)

        cv2.polylines(mouth_image, [mouth_outer_pts], False, (255, 255, 255), thickness=1)
        cv2.polylines(mouth_image, [mouth_inner_pts], False, (255, 255, 255), thickness=1)

        m_h, m_w = 54, 120
        mouth = mouth_image[int(y - b_rate * h):int(y + (1 + b_rate) * h),
                   int(x - b_rate * w):int(x + (1 + b_rate) * w)]
        # mouth = cv2.resize(mouth, (68, 28))
        h, w = mouth.shape[:-1]
        if h > m_h-4 or w > m_w-20:
            mouth = cv2.resize(mouth, (68, 30))
            h, w = mouth.shape[:-1]
        top = buttom = max(0, int((m_h - h) / 2))
        left = right = max(0, int((m_w - w) / 2))
        mouth = cv2.copyMakeBorder(mouth, top, buttom, left, right, cv2.BORDER_CONSTANT, None,
                                             (0, 0, 0))
        # cv2.imshow("img_comb", mouth)
        # cv2.waitKey(30)
        self.mouth_image = mouth


    def get_3D_face_mesh(self, frame):
        output = []
        results = self.face_mesh.process(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
        face_landmarks = results.multi_face_landmarks
        frame_shape = frame.shape
        h, w = frame_shape[:-1]

        if face_landmarks:
            land_pts = []
            landmark = face_landmarks[0]     ## There are total of 468 facial landmark points

            for i in range(478):
                point = landmark.landmark[i]
                x = int(point.x * w)
                y = int(point.y * h)
                land_pts.append((x, y))
                # cv2.circle(annotated_image, (x, y), 2, (0, 255, 0), -1)

            # show the head pose coordinate
            vecroll, annotated_image = self.head_pose_calculation(landmark.landmark, landmark, land_pts, frame_shape)

            # show the gaze direction
            left_eye_center, left_end, right_eye_center, right_end = self.gaze_direction_calculation(vecroll, landmark.landmark, frame_shape)

            # show eyes
            self.show_eyes(land_pts, frame_shape)

            # show mouth
            self.show_mouth(land_pts, frame_shape)

            if self.eye_close==False:
                cv2.arrowedLine(frame, (int(left_eye_center[0] * w), int(left_eye_center[1] * h)),
                                (int(left_end[0] * w), int(left_end[1] * h)),
                                (0, 255, 0), 2)
                cv2.arrowedLine(frame, (int(right_eye_center[0] * w), int(right_eye_center[1] * h)),
                                (int(right_end[0] * w), int(right_end[1] * h)), (0, 0, 255), 2)

            ann_h = 300
            ann_w = 360
            land_pts = np.array(land_pts)
            rx, ry, rw, rh = cv2.boundingRect(land_pts)
            cv2.rectangle(frame, (rx, ry), (rx + rw, ry + rh), (0, 255, 255), 1)
            st_h = max(0, int(ry - 0.4 * rh))
            st_w = max(0, int(rx - 0.5 * rw))
            annotated_image = annotated_image[st_h:int(ry + 1.4 * rh), st_w:int(rx + 1.5 * rw)]
            annotated_image = cv2.resize(annotated_image, (268, 300))
            a_h, a_w = annotated_image.shape[:-1]
            top = buttom = int((ann_h - a_h)/2)
            left = right = int((ann_w - a_w)/2)
            annotated_image = cv2.copyMakeBorder(annotated_image, top, buttom, left, right, cv2.BORDER_CONSTANT, None, (0, 0, 0))
            self.frame = frame
            self.annotated_image = annotated_image

        output.append(self.frame)
        output.append(self.annotated_image)
        output.append(self.left_eye_image)
        output.append(self.right_eye_image)
        output.append(self.mouth_image)

        return output



