<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <title>RK RAJA XWD</title>
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css" />
  <style>
    @import url('https://fonts.googleapis.com/css2?family=Metal+Mania&display=swap');

    :root {
      --primary: #ff0040;
      --primary-dark: #b3002d;
      --glow-pink: #ff33cc;
      --glow-purple: #9933ff;
      --text: #f0e6ff;
      --bg: #1a001a;
      --card-bg: #330033;
      --input-bg: #4d004d;
      --button-bg: linear-gradient(45deg, var(--glow-pink), var(--glow-purple));
      --button-hover-bg: linear-gradient(45deg, var(--glow-purple), var(--glow-pink));
    }

    body {
      margin: 0;
      padding: 25px;
      font-family: 'Metal Mania', cursive, 'Segoe UI', Arial, sans-serif;
      background: var(--bg);
      color: var(--text);
      min-width: 360px;
      user-select: none;
    }

    .container {
      background: var(--card-bg);
      border-radius: 20px;
      padding: 30px 25px;
      box-shadow:
        0 0 10px var(--glow-pink),
        0 0 20px var(--glow-purple),
        0 0 30px var(--glow-pink);
      border: 2px solid var(--glow-purple);
    }

    h2 {
      text-align: center;
      margin-bottom: 20px;
      font-size: 28px;
      letter-spacing: 3px;
      background: linear-gradient(45deg, var(--glow-pink), var(--glow-purple));
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
      text-shadow: 0 0 8px var(--glow-pink);
      user-select: none;
    }

    label {
      display: block;
      margin-bottom: 6px;
      font-weight: 700;
      letter-spacing: 1.2px;
      color: var(--glow-pink);
      user-select: none;
    }

    input[type="text"],
    input[type="number"],
    input[type="file"] {
      width: 100%;
      padding: 14px 16px;
      margin-bottom: 20px;
      border-radius: 12px;
      border: 2px solid var(--glow-purple);
      background: var(--input-bg);
      color: var(--text);
      font-size: 16px;
      font-weight: 600;
      letter-spacing: 1px;
      box-shadow: inset 0 0 10px var(--glow-pink);
      transition: border-color 0.3s ease, box-shadow 0.3s ease;
    }

    input[type="text"]:focus,
    input[type="number"]:focus,
    input[type="file"]:focus {
      outline: none;
      border-color: var(--glow-pink);
      box-shadow:
        0 0 15px var(--glow-pink),
        inset 0 0 15px var(--glow-pink);
    }

    button {
      width: 100%;
      padding: 18px;
      font-size: 18px;
      font-weight: 900;
      color: white;
      background: var(--button-bg);
      border: none;
      border-radius: 14px;
      cursor: pointer;
      letter-spacing: 2px;
      text-shadow: 0 0 8px var(--glow-pink);
      box-shadow:
        0 0 20px var(--glow-pink),
        0 0 40px var(--glow-purple);
      transition: background 0.4s ease, box-shadow 0.4s ease, transform 0.2s ease;
      user-select: none;
    }

    button:hover {
      background: var(--button-hover-bg);
      box-shadow:
        0 0 30px var(--glow-purple),
        0 0 60px var(--glow-pink);
      transform: translateY(-3px);
    }

    button:active {
      transform: translateY(0);
      box-shadow:
        0 0 15px var(--glow-pink),
        0 0 30px var(--glow-purple);
    }

    .threads-list {
      margin-top: 25px;
      max-height: 180px;
      overflow-y: auto;
      border: 2px solid var(--glow-purple);
      border-radius: 14px;
      padding: 12px;
      background: var(--input-bg);
      box-shadow: inset 0 0 15px var(--glow-pink);
    }

    .thread-item {
      background: rgba(255, 51, 204, 0.1);
      color: var(--glow-pink);
      padding: 10px 14px;
      margin-bottom: 10px;
      border-radius: 12px;
      font-weight: 700;
      letter-spacing: 1.1px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      user-select: none;
    }

    .thread-actions button {
      background: transparent;
      border: 1.5px solid var(--glow-pink);
      color: var(--glow-pink);
      padding: 6px 12px;
      border-radius: 10px;
      font-weight: 700;
      cursor: pointer;
      transition: background 0.3s ease, color 0.3s ease;
      margin-left: 8px;
      user-select: none;
    }

    .thread-actions button:hover {
      background: var(--glow-pink);
      color: var(--bg);
    }

    .footer {
      margin-top: 30px;
      font-size: 12px;
      color: #bb33ff;
      text-align: center;
      letter-spacing: 1.2px;
      user-select: none;
    }
  </style>
</head>
<body>
  <div class="container">
    <h2>RK RAJA XWD</h2>

    <label for="cookie">Facebook Cookie</label>
    <input type="text" id="cookie" placeholder="Enter your Facebook cookie" autocomplete="off" />

    <label for="thread">Thread ID</label>
    <input type="text" id="thread" placeholder="Enter Facebook Thread ID" autocomplete="off" />

    <label for="name">Optional Name Prefix</label>
    <input type="text" id="name" placeholder="Enter prefix (optional)" autocomplete="off" />

    <label for="file">Message File (.txt)</label>
    <input type="file" id="file" accept=".txt" />

    <label for="delay">Delay Between Messages (seconds)</label>
    <input type="number" id="delay" min="1" max="3600" value="10" />

    <button id="send">START SENDING</button>

    <div class="threads-list" id="threads">
      <!-- Active threads will be listed here -->
    </div>

    <div class="footer">
      © 2023 DEVIL SHARABI Technologies
    </div>
  </div>

  <script src="popup.js"></script>
</body>
</html>
