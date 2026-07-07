import tempfile
import os
from playwright.sync_api import sync_playwright
class PlaywrightProvider:
    def authenticate(self):
        profile_dir = os.path.join(tempfile.gettempdir(), "lc_secure_auth_ctx")
        
        with sync_playwright() as p:
            print("[*] Spawning secure execution frame...")
            
            context = p.chromium.launch_persistent_context(
                user_data_dir=profile_dir,
                headless=False,
                no_viewport=True,
                ignore_default_args=["--enable-automation"], 
                args=[
                    "--disable-blink-features=AutomationControlled",
                    "--disable-infobars",
                    "--start-maximized"
                ]
            )
            
            page = context.pages[0] if context.pages else context.new_page()
            
            # Bypass navigator blocks
            page.add_init_script("""
                Object.defineProperty(navigator, 'webdriver', {
                    get: () => undefined
                });
            """)
            
            print("[*] Contacting LeetCode Gateway...")
            page.goto("https://leetcode.com/accounts/login/", wait_until="load")
            
            print("\n========================================================")
            print("[!] ACTION REQUIRED: Please fill in details and Log In manually.")
            print("========================================================")
            print("[*] Waiting for successful authentication backend event...")

            session_id = None
            csrf_token = None
            
            # We loop and actively check for cookies every second instead of watching URLs
            max_attempts = 180  # 3-minute limit
            for _ in range(max_attempts):
                page.wait_for_timeout(1000) # Check every 1 second
                
                cookies = context.cookies()
                for cookie in cookies:
                    if cookie['name'] == 'LEETCODE_SESSION':
                        session_id = cookie['value']
                    elif cookie['name'] == 'csrftoken':
                        csrf_token = cookie['value']
                
                # The exact instant we find the session cookie, break out immediately!
                if session_id:
                    print("\n[+] Success! Captured live authentication state from browser memory.")
                    break
            else:
                print("\n[-] Timeout Error: Login was not detected within 3 minutes.")
                    
            context.close()
            
            return {
                "LEETCODE_SESSION": session_id,
                "csrftoken": csrf_token
            }

    if __name__ == "__main__":
        tokens = authenticate()
        if tokens and tokens["LEETCODE_SESSION"]:
            print("\n🎉 EXTRACTED TOKENS SUCCESSFULLY:")
            print(f"LEETCODE_SESSION = {tokens['LEETCODE_SESSION']}")
            print(f"csrftoken        = {tokens['csrftoken']}")
        else:
            print("\n❌ Failed to capture tokens.")