import os
import sys
import cv2



def save_videos(images, output_name, fps=10):
    if not images:
        print("there is no image")
        return
    os.makedirs(os.path.split(output_name)[0], exist_ok=True)

    h, w, _ = images[0].shape
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    video_writer = cv2.VideoWriter(output_name, fourcc, fps, (w, h))
    
    for image in images:
        video_writer.write(image)
    
    video_writer.release()
    print(f'Videos saved in {output_name}') 


def save_images(images, output_path):
    if not images:
        print("there is no image")
        return
    os.makedirs(output_path, exist_ok=True)

    for index, arr in enumerate(images):
        output_name = os.path.join(output_path, f'traj_{index:06d}.png')
        cv2.imwrite(output_name, arr)
    imgs_num = len(images)
    print(f'{imgs_num} Images saved in {output_path}')


def save_results(info, output_path):
    os.makedirs(os.path.split(output_path)[0], exist_ok=True)
    with open(output_path, 'w') as f:
        f.writelines(info)
        print('Eval results saved in {output_path}')


def interactive(tasks):
    print("Server: Input task is invalid.")
    print("Please re-input a task name from the list:")
    for key, value in tasks.items():
        print(f"{key}: {value}")
    print("All: Run all tasks\r\nesc: Exit\r\n")
    while True:
        user_input = input("Enter task name: ")
        
        if user_input.lower() == 'esc':
            sys.exit()

        if user_input.lower() == 'all':
            return list(tasks.keys())
        
        elif user_input in tasks.keys():
            return [user_input]
        else:
            print("Server: Input task is invalid.")
            print("Please re-input a task name. ")   