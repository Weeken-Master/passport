# import time
# from pynput.mouse import Controller

# # Tạo đối tượng điều khiển chuột
# mouse = Controller()

# try:
#     while True:
#         # Lấy tọa độ hiện tại của chuột
#         current_position = mouse.position
#         print(f"Tọa độ hiện tại của chuột là: {current_position}")
        
#         # Chờ 1 giây trước khi lấy tọa độ lần tiếp theo
#         time.sleep(1)
# except KeyboardInterrupt:
#     print("Đã dừng việc giám sát tọa độ chuột.")


import pyautogui
pyautogui.click(1169,668)