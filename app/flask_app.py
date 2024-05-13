from flask import Flask, render_template, request
from file_tools import download_youtube_video, convert_to_mp3

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        youtube_url = request.form['youtube_url']
        output_filename = 'video'  # Default output filename
        download_success = download_youtube_video(youtube_url, output_filename)
        if download_success:
            mp3_file = convert_to_mp3(output_filename + '.mp4', output_filename)
            if mp3_file:
                message = f"Conversion successful! MP3 file saved as {mp3_file}"
                return render_template('home.html', message=message, mp3_file=mp3_file)
            else:
                message = "Conversion failed. Please try again."
                return render_template('home.html', message=message)
        else:
            message = "Failed to download the video. Please check the URL and try again."
            return render_template('home.html', message=message)
    return render_template('home.html')

if __name__ == '__main__':
    app.run(debug=True)
