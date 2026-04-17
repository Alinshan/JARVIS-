# actions/send_message.py
# Universal messaging & calls — WhatsApp, Telegram, Instagram
# Uses visual element detection (pyautogui) for cross-platform automation.

import time
import pyautogui
import pyperclip
from pathlib import Path

pyautogui.FAILSAFE = True
pyautogui.PAUSE = 0.08

def _open_app(app_name: str) -> bool:
    """Opens an app via Windows search."""
    try:
        pyautogui.press("win")
        time.sleep(0.4)
        pyautogui.write(app_name, interval=0.04)
        time.sleep(0.5)
        pyautogui.press("enter")
        time.sleep(2.0)  
        return True
    except Exception as e:
        print(f"[CommController] Could not open {app_name}: {e}")
        return False


def _search_contact(contact: str):
    """Searches for a contact inside a messaging app."""
    # Ensure any open overlays are closed
    pyautogui.press("esc")
    time.sleep(0.3)
    
    # Focus search bar
    pyautogui.hotkey("ctrl", "f")
    time.sleep(0.5)
    
    # Clear and type
    pyautogui.hotkey("ctrl", "a")
    pyautogui.press("backspace")
    time.sleep(0.2)
    pyautogui.write(contact, interval=0.04)
    
    # Wait for search results to populate
    time.sleep(1.5) 
    pyautogui.press("enter")
    time.sleep(1.0) # Wait for conversation to load


def _send_whatsapp(receiver: str, message: str) -> str:
    """Sends a WhatsApp message via the Windows desktop app."""
    try:
        if not _open_app("WhatsApp"):
            return "Could not open WhatsApp."

        print(f"[JARVIS] 📨 Preparing message for {receiver}...")
        time.sleep(1.0)
        _search_contact(receiver)

        # Use clipboard for maximum reliability
        pyperclip.copy(message)
        time.sleep(0.2)
        pyautogui.hotkey("ctrl", "v")
        time.sleep(0.3)
        pyautogui.press("enter")

        return f"Message sent to {receiver} via WhatsApp."
    except Exception as e:
        return f"WhatsApp send error: {e}"


def _call_whatsapp(receiver: str, call_type: str = "voice") -> str:
    """Initiates a WhatsApp call via the Windows desktop app."""
    try:
        if not _open_app("WhatsApp"):
            return "Could not open WhatsApp."

        print(f"[JARVIS] 📞 Initiating {call_type} call to {receiver}...")
        time.sleep(1.0)
        _search_contact(receiver)

        # Official WhatsApp Desktop Shortcuts:
        # Voice Call: Ctrl + Shift + C
        # Video Call: Ctrl + Shift + V
        if "video" in call_type.lower():
            pyautogui.hotkey("ctrl", "shift", "v")
            mode = "Video call"
        else:
            pyautogui.hotkey("ctrl", "shift", "c")
            mode = "Voice call"

        time.sleep(0.5)
        return f"{mode} initiated with {receiver} on WhatsApp."
    except Exception as e:
        return f"WhatsApp call error: {e}"


def whatsapp_control(
    parameters: dict,
    player=None
) -> str:
    """
    Centralized tool for WhatsApp operations: open, send, call.
    """
    params    = parameters or {}
    action    = params.get("action", "send").strip().lower()
    receiver  = params.get("receiver", "").strip()
    message   = params.get("message", "").strip()
    call_type = params.get("call_type", "voice").strip().lower()

    log_msg = f"[whatsapp] {action} -> {receiver}"
    if player:
        player.write_log(log_msg)
        player.write_log("⚠️ PLEASE DO NOT MOVE MOUSE OR KEYBOARD")

    if action == "open":
        if _open_app("WhatsApp"):
            return "WhatsApp opened successfully, sir."
        return "Failed to open WhatsApp."

    if not receiver:
        return "Please specify a contact, sir."

    if action == "call":
        return _call_whatsapp(receiver, call_type)
    
    if action == "send":
        if not message:
            return "What message should I send, sir?"
        return _send_whatsapp(receiver, message)

    return f"Unknown WhatsApp action: {action}"


# --- Legacy / Other Platforms ---

def _send_instagram(receiver: str, message: str) -> str:
    try:
        import webbrowser
        webbrowser.open("https://www.instagram.com/direct/new/")
        time.sleep(3.5)
        
        pyperclip.copy(receiver)
        pyautogui.hotkey("ctrl", "v")
        time.sleep(1.5)
        
        pyautogui.press("down")
        time.sleep(0.3)
        pyautogui.press("enter")
        time.sleep(0.5)
        for _ in range(3):
            pyautogui.press("tab")
            time.sleep(0.1)
        pyautogui.press("enter")
        time.sleep(1.5)
        
        pyperclip.copy(message)
        pyautogui.hotkey("ctrl", "v")
        time.sleep(0.2)
        pyautogui.press("enter")
        return f"Message sent to {receiver} via Instagram."
    except Exception as e:
        return f"Instagram error: {e}"

def _send_telegram(receiver: str, message: str) -> str:
    try:
        if not _open_app("Telegram"):
            return "Could not open Telegram."
        time.sleep(1.5)
        _search_contact(receiver)
        
        pyperclip.copy(message)
        pyautogui.hotkey("ctrl", "v")
        time.sleep(0.2)
        pyautogui.press("enter")
        return f"Message sent to {receiver} via Telegram."
    except Exception as e:
        return f"Telegram error: {e}"

def send_message(
    parameters: dict,
    response=None,
    player=None,
    session_memory=None
) -> str:
    """Compatibility layer for existing send_message calls."""
    params       = parameters or {}
    receiver     = params.get("receiver", "").strip()
    message_text = params.get("message_text", "").strip()
    platform     = params.get("platform", "whatsapp").strip().lower()

    if "whatsapp" in platform:
        return whatsapp_control({"action": "send", "receiver": receiver, "message": message_text}, player)
    
    if "instagram" in platform:
        return _send_instagram(receiver, message_text)
    
    if "telegram" in platform:
        return _send_telegram(receiver, message_text)

    return f"Platform {platform} not fully supported yet for advanced control."