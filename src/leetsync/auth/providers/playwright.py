# from datetime import datetime
# from leetsync.auth.models import AuthSession
# import tempfile
# import os
# from playwright.sync_api import sync_playwright
# class PlaywrightProvider:
#     def authenticate(self):
#         profile_dir = os.path.join(tempfile.gettempdir(), "lc_secure_auth_ctx")
        
#         with sync_playwright() as p:
#             print("[*] Spawning secure execution frame...")
            
#             context = p.chromium.launch_persistent_context(
#                 user_data_dir=profile_dir,
#                 headless=False,
#                 no_viewport=True,
#                 ignore_default_args=["--enable-automation"], 
#                 args=[
#                     "--disable-blink-features=AutomationControlled",
#                     "--disable-infobars",
#                     "--start-maximized"
#                 ]
#             )
            
#             page = context.pages[0] if context.pages else context.new_page()
            
#             # Bypass navigator blocks
#             page.add_init_script("""
#                 Object.defineProperty(navigator, 'webdriver', {
#                     get: () => undefined
#                 });
#             """)
            
#             print("[*] Contacting LeetCode Gateway...")
#             page.goto("https://leetcode.com/accounts/login/", wait_until="load")
            
#             print("\n========================================================")
#             print("[!] ACTION REQUIRED: Please fill in details and Log In manually.")
#             print("========================================================")
#             print("[*] Waiting for successful authentication backend event...")

#             session_id = None
#             csrf_token = None
            
#             # We loop and actively check for cookies every second instead of watching URLs
#             max_attempts = 180  # 3-minute limit
#             for _ in range(max_attempts):
#                 page.wait_for_timeout(1000) # Check every 1 second
                
#                 cookies = context.cookies()
#                 for cookie in cookies:
#                     if cookie['name'] == 'LEETCODE_SESSION':
#                         session_id = cookie['value']
#                     elif cookie['name'] == 'csrftoken':
#                         csrf_token = cookie['value']
                
#                 # The exact instant we find the session cookie, break out immediately!
#                 if session_id:
#                     print("\n[+] Success! Captured live authentication state from browser memory.")
#                     break
#             else:
#                 print("\n[-] Timeout Error: Login was not detected within 3 minutes.")
                    
#             context.close()
            
#             return AuthSession(
#                     username="",      # temporary
#                     cookies={
#                     "LEETCODE_SESSION": session_id,
#                     "csrftoken": csrf_token,
#                             },
#                     authenticated_at=datetime.now(),
#                             )

# if __name__ == "__main__":
#     # Create an instance of the provider class
#     provider = PlaywrightProvider()
    
#     # Call the instance method
#     tokens = provider.authenticate()
    
#     if tokens and tokens["LEETCODE_SESSION"]:
#         print("\n🎉 EXTRACTED TOKENS SUCCESSFULLY:")
#         print(f"LEETCODE_SESSION = {tokens['LEETCODE_SESSION']}")
#         print(f"csrftoken        = {tokens['csrftoken']}")
#     else:
#         print("\n❌ Failed to capture tokens.")

# from datetime import datetime
# from leetsync.auth.models import AuthSession
# import os
# from playwright.sync_api import sync_playwright

# class PlaywrightProvider:
#     def authenticate(self) -> AuthSession | None:
#         # ✅ FIXED: Permanent local folder inside project structure instead of volatile tempdir
#         # This keeps you signed in permanently across sequential framework restarts!
#         profile_dir = os.path.abspath(".leetcode_session")
        
#         with sync_playwright() as p:
#             print("[*] Spawning secure execution frame...")
            
#             context = p.chromium.launch_persistent_context(
#                 user_data_dir=profile_dir,
#                 headless=False,
#                 no_viewport=True,
#                 ignore_default_args=["--enable-automation"], 
#                 args=[
#                     "--disable-blink-features=AutomationControlled",
#                     "--disable-infobars",
#                     "--start-maximized"
#                 ]
#             )
            
#             page = context.pages[0] if context.pages else context.new_page()
            
#             # Bypass navigator blocks
#             page.add_init_script("""
#                 Object.defineProperty(navigator, 'webdriver', {
#                     get: () => undefined
#                 });
#             """)
            
#             print("[*] Contacting LeetCode Gateway...")
#             page.goto("https://leetcode.com/accounts/login/", wait_until="load")
            
#             # Quick check if cookies are already loaded from memory layer
#             cookies = context.cookies()
#             session_id = next((c['value'] for c in cookies if c['name'] == 'LEETCODE_SESSION'), None)
#             csrf_token = next((c['value'] for c in cookies if c['name'] == 'csrftoken'), None)
            
#             if session_id:
#                 print("[+] Active authenticated session found in cache profile storage. Bypassing manual login prompt.")
#             else:
#                 print("\n========================================================")
#                 print("[!] ACTION REQUIRED: Please fill in details and Log In manually.")
#                 print("========================================================")
#                 print("[*] Waiting for successful authentication backend event...")

#                 max_attempts = 180  # 3-minute limit
#                 for _ in range(max_attempts):
#                     page.wait_for_timeout(1000) # Check every 1 second
                    
#                     cookies = context.cookies()
#                     for cookie in cookies:
#                         if cookie['name'] == 'LEETCODE_SESSION':
#                             session_id = cookie['value']
#                         elif cookie['name'] == 'csrftoken':
#                             csrf_token = cookie['value']
                    
#                     if session_id:
#                         print("\n[+] Success! Captured live authentication state from browser memory.")
#                         break
#                 else:
#                     print("\n[-] Timeout Error: Login was not detected within 3 minutes.")
                    
#             context.close()
            
#             if session_id:
#                 return AuthSession(
#                     username="tarun100ni",
#                     cookies={
#                         "LEETCODE_SESSION": session_id,
#                         "csrftoken": csrf_token,
#                     },
#                     authenticated_at=datetime.now(),
#                 )
#             return None

# if __name__ == "__main__":
#     provider = PlaywrightProvider()
#     tokens = provider.authenticate()
    
#     # ✅ FIXED: Avoided dict-based access crash on AuthSession instance wrapper
#     if tokens and tokens.cookies.get("LEETCODE_SESSION"):
#         print("\n🎉 EXTRACTED TOKENS SUCCESSFULLY:")
#         print(f"LEETCODE_SESSION = {tokens.cookies['LEETCODE_SESSION']}")
#         print(f"csrftoken        = {tokens.cookies['csrftoken']}")
#     else:
#         print("\n❌ Failed to capture tokens.")
from datetime import datetime
from leetsync.auth.models import AuthSession
import os
from playwright.sync_api import sync_playwright

class PlaywrightProvider:
    def authenticate(self) -> AuthSession | None:
        # ✅ Persistent profile context structure mapping inside workspace root
        profile_dir = os.path.abspath(".leetcode_session")
        
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
            
            # Anti-bot trigger bypass script injection
            page.add_init_script("""
                Object.defineProperty(navigator, 'webdriver', {
                    get: () => undefined
                });
            """)
            
            print("[*] Contacting LeetCode Gateway...")
            page.goto("https://leetcode.com/accounts/login/", wait_until="load")
            
            # Instant memory verification layer check
            cookies = context.cookies()
            session_id = next((c['value'] for c in cookies if c['name'] == 'LEETCODE_SESSION'), None)
            csrf_token = next((c['value'] for c in cookies if c['name'] == 'csrftoken'), None)
            
            if session_id:
                print("[+] Active authenticated session found in cache profile storage. Bypassing manual login prompt.")
            else:
                print("\n========================================================")
                print("[!] ACTION REQUIRED: Please fill in details and Log In manually.")
                print("========================================================")
                print("[*] Waiting for successful authentication backend event...")

                max_attempts = 180  # 3-minute max manual gate
                for _ in range(max_attempts):
                    page.wait_for_timeout(1000) 
                    
                    cookies = context.cookies()
                    for cookie in cookies:
                        if cookie['name'] == 'LEETCODE_SESSION':
                            session_id = cookie['value']
                        elif cookie['name'] == 'csrftoken':
                            csrf_token = cookie['value']
                    
                    if session_id:
                        print("\n[+] Success! Captured live authentication state from browser memory.")
                        break
                else:
                    print("\n[-] Timeout Error: Login was not detected within 3 minutes.")
                    
            context.close()
            
            if session_id:
                return AuthSession(
                    username="tarun100ni",
                    cookies={
                        "LEETCODE_SESSION": session_id,
                        "csrftoken": csrf_token,
                    },
                    authenticated_at=datetime.now(),
                )
            return None

if __name__ == "__main__":
    provider = PlaywrightProvider()
    tokens = provider.authenticate()
    
    if tokens and tokens.cookies.get("LEETCODE_SESSION"):
        print("\n🎉 EXTRACTED TOKENS SUCCESSFULLY:")
        print(f"LEETCODE_SESSION = {tokens.cookies['LEETCODE_SESSION']}")
        print(f"csrftoken        = {tokens.cookies['csrftoken']}")
    else:
        print("\n❌ Failed to capture tokens.")