import ffmpeg
import os

def convert_file(input_file, output_file):
    try:
        (
            ffmpeg
            .input(input_file, fflags='+genpts')
            .output(output_file, **{'c:v': 'copy', 'c:a': 'copy'}, fflags='+genpts+discardcorrupt')
            .run(overwrite_output=True)
        )
        print(f"File was successfuly saved as {output_file}")
    except ffmpeg.Error as e:
        error_message = e.stderr.decode() if e.stderr else "unknown error"
        print(f"Error: {error_message}")

def process_directory(input_dir, output_dir):
    # Создаем выходную папку, если она не существует
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Проходим по всем файлам в исходной папке
    for filename in os.listdir(input_dir):
        input_file = os.path.join(input_dir, filename)

        # Проверяем, является ли файл видеофайлом
        if input_file.lower().endswith(('.avi')): # .mp4, mp3 etc.
            output_file = os.path.join(output_dir, os.path.splitext(filename)[0] + '.mkv')
            convert_file(input_file, output_file)

if __name__ == "__main__":
    input_dir = input("Source folder: ")
    output_dir = input("Target folder: ")
    process_directory(input_dir, output_dir)