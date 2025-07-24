# BrandKit

A comprehensive brand management toolkit for creating, managing, and maintaining consistent brand assets and guidelines.

## Description

BrandKit is a modern, user-friendly application designed to help businesses and individuals manage their brand assets efficiently. Whether you're a designer, marketer, or business owner, BrandKit provides the tools you need to maintain brand consistency across all your projects.

## Features

- 🎨 **Brand Asset Management** - Organize and store logos, colors, fonts, and other brand elements
- 📋 **Style Guide Generation** - Create comprehensive brand style guides automatically
- 🎯 **Brand Consistency Tools** - Ensure your brand stays consistent across all touchpoints
- 📱 **Multi-Platform Support** - Access your brand assets from anywhere
- 🔄 **Version Control** - Track changes to your brand assets over time
- 👥 **Team Collaboration** - Share brand guidelines with your team
- 📊 **Analytics & Insights** - Track how your brand assets are being used

## Getting Started

### Prerequisites

- Node.js (v16 or higher)
- npm or yarn package manager
- Python 3.8 or higher
- Docker and Docker Compose (for containerized development)

### Installation

#### Option 1: Using Docker (Recommended)

1. Clone the repository:
```bash
git clone https://github.com/bsamson01/brandkit.git
cd brandkit
```

2. Build and start the application with Docker:
```bash
docker-compose up --build
```

3. Set up environment variables (optional for backend):
   ```bash
   cp .env.example .env
   # Edit .env and add your OpenAI API key for backend functionality
   ```

4. Open your browser and navigate to:
   - Frontend: `http://localhost:3001`
   - Backend API: `http://localhost:8001`

The application will automatically reload when you make changes to the source code.

**Note:** The backend requires an OpenAI API key to function. If you don't have one, the frontend will still work independently.

#### Option 2: Local Development

1. Clone the repository:
```bash
git clone https://github.com/bsamson01/brandkit.git
cd brandkit
```

2. Install frontend dependencies:
```bash
cd frontend
npm install
```

3. Install backend dependencies:
```bash
pip install -r requirements.txt
```

4. Start the development servers:
   - Frontend: `cd frontend && npm run dev`
   - Backend: `cd backend && python main.py`

## Usage

[Usage instructions will be added as the project develops]

## Contributing

We welcome contributions! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

1. Fork the project
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

- GitHub: [@bsamson01](https://github.com/bsamson01)
- Project Link: [https://github.com/bsamson01/brandkit](https://github.com/bsamson01/brandkit)

## Acknowledgments

- Thanks to all contributors who will help make BrandKit better
- Inspired by the need for better brand management tools in the digital age
