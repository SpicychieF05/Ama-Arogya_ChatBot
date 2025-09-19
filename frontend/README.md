# Odisha Health Chatbot - Frontend Demo

This directory contains the web-based demo interface for the Ama Arogya (Odisha Health Chatbot) project.

## Files

- `index.html` - Main HTML structure for the demo interface
- `styles.css` - CSS styles and responsive design
- `script.js` - JavaScript functionality for chat interface and API integration

## Features

### 🎨 Modern UI/UX
- Clean, responsive design optimized for mobile and desktop
- Gradient backgrounds and smooth animations
- Professional chat interface with typing indicators

### 💬 Interactive Chat Demo
- Real-time chat interface that connects to the FastAPI backend
- Support for English, Hindi, and Odia languages
- Quick question buttons for easy testing
- Typing indicators and message animations

### 📱 Responsive Design
- Mobile-first design approach
- Phone mockup visualization in hero section
- Optimized for various screen sizes

### 🚀 Live Demo Features
- Automatic server status detection
- Fallback demo responses when server is offline
- Sample queries in multiple languages
- Real-time language switching

## How to Use

1. **Start the Backend Server:**
   ```bash
   cd /path/to/Odisha_ChatBot
   source .venv/Scripts/activate  # or .venv/bin/activate on Unix
   uvicorn main:app --host 0.0.0.0 --port 8001 --reload
   ```

2. **Access the Demo:**
   - Main demo interface: http://localhost:8001/
   - Direct demo page: http://localhost:8001/demo
   - API docs: http://localhost:8001/docs
   - Analytics dashboard: http://localhost:8001/dashboard

3. **Test the Chatbot:**
   - Use the chat interface in the "Live Demo" section
   - Try sample queries in different languages
   - Switch between English, Hindi, and Odia
   - Click on suggested queries for quick testing

## Demo Capabilities

### Health Topics Supported:
- **Fever & Symptoms:** Basic symptom assessment and advice
- **Vaccination:** Complete immunization schedules for children
- **Maternal Care:** Pregnancy and prenatal care guidance
- **General Health:** Health tips and preventive care information

### Language Support:
- **English:** Full health information and guidance
- **Hindi (हिंदी):** Localized health advice in Hindi
- **Odia (ଓଡ଼ିଆ):** Native language support for Odisha residents

### Interactive Elements:
- Quick question buttons
- Language selector
- Real-time connection status
- Typing indicators
- Message timestamps
- Sample query suggestions

## Technical Details

### Frontend Stack:
- **HTML5:** Semantic markup and accessibility
- **CSS3:** Modern styling with Grid and Flexbox
- **Vanilla JavaScript:** No external dependencies
- **Font Awesome:** Icons and visual elements
- **Google Fonts:** Typography (Inter font family)

### API Integration:
- RESTful API calls to FastAPI backend
- JSON request/response handling
- Error handling and fallback responses
- Real-time server status checking

### Offline Capability:
- Demo mode when backend is unavailable
- Simulated responses for testing
- Graceful degradation of features

## Customization

### Styling:
- Modify `styles.css` for visual customization
- Update color scheme in CSS variables
- Adjust responsive breakpoints as needed

### Content:
- Update sample queries in `script.js`
- Modify welcome messages for different languages
- Add new demo response patterns

### Functionality:
- Extend API integration in `script.js`
- Add new interactive features
- Implement additional language support

## Browser Compatibility

- **Modern Browsers:** Chrome 80+, Firefox 75+, Safari 13+, Edge 80+
- **Mobile Browsers:** iOS Safari 13+, Chrome Mobile 80+
- **Features Used:** CSS Grid, Flexbox, Fetch API, ES6+ JavaScript

## Performance

- **Optimized Assets:** Compressed images and efficient CSS
- **Lazy Loading:** Progressive enhancement approach
- **Minimal Dependencies:** Only essential external resources
- **Fast Loading:** Optimized for slow network connections

This demo interface effectively showcases the capabilities of the Odisha Health Chatbot and provides an intuitive way for users to interact with the AI-powered health assistant.