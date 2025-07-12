# E-Paper User Info Display

This Arduino sketch has been enhanced to display personalized user information (Slack handle and full name) on the e-paper display.

## Features

- **Dynamic Text Display**: Shows your Slack handle and full name on the e-paper screen
- **Serial Control**: Update user info via Serial Monitor commands
- **Toggle Mode**: Switch between user info display and original image
- **Responsive Layout**: Automatically centers text with proper padding
- **Large Text**: Uses 16x16 pixel font for clear readability

## Display Layout

The user info takes up the full width (128px) and half the height (148px) of the screen:

```
┌─────────────────────────────────┐
│          (10px padding)         │
│                                 │
│        @your.slackhandle        │
│                                 │
│        ─────────────────        │  ← separator line
│                                 │
│         Your Full Name          │
│                                 │
│          (10px padding)         │
└─────────────────────────────────┘
```

## Quick Start

1. **Set your info in code** (lines 42-44):
   ```cpp
   String slackHandle = "@your.handle";
   String fullName = "Your Full Name";
   bool displayUserInfo = true;
   ```

2. **Upload the sketch** to your Arduino

3. **Open Serial Monitor** (115200 baud) to see available commands

## Serial Commands

Connect via Serial Monitor at **115200 baud** and use these commands:

| Command | Example | Description |
|---------|---------|-------------|
| `slack:<handle>` | `slack:@alice.smith` | Update Slack handle |
| `name:<fullname>` | `name:Alice Smith` | Update full name |
| `show` | `show` | Display current settings and refresh screen |
| `toggle` | `toggle` | Switch between user info and original image |

## Programming Interface

### Update User Info Programmatically

```cpp
// Update both handle and name at once
updateUserInfo("@new.handle", "New Full Name");

// Or update variables individually
slackHandle = "@updated.handle";
fullName = "Updated Name";
showUserInfo(); // Refresh display
```

### Toggle Display Mode

```cpp
displayUserInfo = false;  // Show original image
displayUserInfo = true;   // Show user info
```

## Technical Details

- **Screen Resolution**: 128x296 pixels
- **Font Size**: 8x8 base font, scaled 2x for 16x16 display
- **Text Encoding**: Supports printable ASCII characters (32-126)
- **Memory Usage**: Allocates temporary buffer for display generation
- **Update Speed**: Uses fast refresh mode for quick updates

## Customization

### Modify Text Positioning

Edit the `createUserInfoDisplay()` function to adjust:
- Vertical positions (currently line 50 and 200)
- Padding amount (currently 10px)
- Separator line styling

### Add More Text Elements

You can extend the display to show additional information by:
1. Adding new String variables
2. Extending the `createUserInfoDisplay()` function
3. Adding new Serial commands in `handleSerialCommand()`

### Change Font Size

Modify the `drawTextLarge()` function to use different scaling:
- Current: 2x scale (16x16 pixels per character)
- For 3x scale: Change the nested loops to use `dx < 3` and `dy < 3`

## Hardware Requirements

- Arduino compatible board with SPI
- GDEY029T94 e-paper display
- NeoPixel strips (optional, for LED effects)

## Pin Connections

| Function | Pin |
|----------|-----|
| EPD BUSY | 9 |
| EPD RES  | 10 |
| EPD DC   | 11 |
| EPD CS   | 13 |
| EPD MISO | 12 |
| EPD MOSI | 15 |
| EPD SCK  | 14 |

## Troubleshooting

- **Text too long**: Text is automatically truncated with "..." if it exceeds display width
- **Display not updating**: Check serial connections and ensure `displayUserInfo` is set to `true`
- **Garbled text**: Verify character encoding is within ASCII printable range
- **Memory issues**: Ensure sufficient RAM is available for display buffer allocation

## Example Usage Session

```
==========================================
    E-Paper User Info Display Ready!
==========================================
Commands:
  slack:<handle>  - Set Slack handle (e.g., slack:@john.doe)
  name:<fullname> - Set full name (e.g., name:John Doe)
  show            - Display current user info
  toggle          - Toggle between user info and original image
==========================================

> slack:@alice.wonderland
Slack handle updated to: @alice.wonderland

> name:Alice Wonderland
Full name updated to: Alice Wonderland

> show
Current settings:
  Slack handle: @alice.wonderland
  Full name: Alice Wonderland
  Display mode: User Info
```
