# 🎵 Face Recognition Music Player

A real-time web application that detects your facial expressions and plays music based on your mood!

## Features

✨ **Real-time Face Detection** - Uses advanced AI to detect your face
😊 **Emotion Recognition** - Identifies moods: Happy, Sad, Angry, Neutral/Calm
🎶 **Auto Music Selection** - Automatically plays different songs based on detected mood
🎯 **Manual Control** - Manually select mood and music preference
🎨 **Beautiful UI** - Modern, responsive interface
⚡ **Zero Setup Required** - Works directly in the browser

## Supported Moods

1. **😊 Happy** - Upbeat, energetic music
2. **😢 Sad** - Melancholic, emotional music
3. **😠 Angry** - Heavy, intense music
4. **😐 Calm/Neutral** - Peaceful, ambient music

## How to Use

### Starting the Server

**Option 1: Python Server (Recommended)**

```bash
python server.py
```

The server will automatically open in your browser at `http://localhost:8000`

**Option 2: Python Built-in HTTP Server**

```bash
python -m http.server 8000
```

Then open `http://localhost:8000` in your browser

**Option 3: Using Node.js (if installed)**

```bash
npx http-server -p 8000
```

### Using the Application

1. **Click "Start Camera"** - Grant camera permission when prompted
2. **Face the Camera** - The AI will detect your face and analyze expressions
3. **Automatic Music** - Music will automatically change based on detected mood
4. **Manual Selection** - Use the mood buttons to manually select music
5. **Enjoy** - Listen with the built-in audio player or your speakers

## Technology Stack

- **Frontend**: HTML5, CSS3, Vanilla JavaScript
- **Face Detection**: face-api.js (TensorFlow.js based)
- **Emotion Recognition**: Deep Learning Neural Networks
- **Audio**: HTML5 Audio API
- **Server**: Python HTTP Server / Node.js

## Browser Compatibility

- ✅ Chrome/Edge (Recommended)
- ✅ Firefox
- ✅ Safari (macOS/iOS)
- ⚠️ Requires HTTPS on production (due to camera access)

## Requirements

- A working webcam
- Modern web browser with JavaScript enabled
- Stable internet connection (for loading ML models)
- Microphone optional (for testing audio)

## Music Sources

The application comes with placeholder music links. You can:

- Replace URLs in the musicDatabase object to use your own songs
- Use any publicly available audio URL
- Host music files in the same directory

Example:

```javascript
const musicDatabase = {
  happy: [{ name: "Your Song", url: "path/to/your/music.mp3", emoji: "🎉" }],
};
```

## Testing Checklist

- [x] Face detection works
- [x] Emotion recognition active
- [x] Music plays on mood change
- [x] Manual mood selection works
- [x] Camera start/stop functions
- [x] Responsive design
- [x] Error handling implemented

## Troubleshooting

### "No face detected"

- Ensure good lighting
- Position face directly toward camera
- Check camera permissions
- Keep face visible in frame

### "Models loading takes long"

- First load takes 10-30 seconds
- Models are cached in browser after first load
- Check internet connection

### Audio doesn't play

- Check browser volume
- Enable autoplay in browser settings
- Check browser console for errors

### Camera permission denied

- Check browser camera permissions
- Try incognito/private mode
- Restart browser

## Project Structure

```
Facemusicapp/
├── index.html      # Main application file
├── server.py       # Python HTTP server
└── README.md       # This file
```

## License

Created for educational purposes. Music samples are placeholder links.

## Features Coming Soon

- Voice mood detection
- Playlist creation
- Mood history tracking
- Custom music upload
- Multi-face detection

---

**Enjoy your mood-based music experience! 🎵**
