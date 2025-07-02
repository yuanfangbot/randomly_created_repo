# Getting Started with Hexo

Hexo is a fast, simple & powerful blog framework built with Node.js.

## Installation

1. Install Node.js
2. Install Hexo
   ```bash
   npm install -g hexo
   ```
3. Create a new blog
   ```bash
   hexo init blog
   cd blog
   npm install
   hexo server
   ```

## Configuration

- `_config.yml`: Main configuration file
- `themes/`: Themes directory
- `source/`: Content source directory

## Deployment

1. Generate static files
   ```bash
   hexo generate
   ```
2. Deploy to GitHub Pages
   ```bash
   hexo deploy
   ```