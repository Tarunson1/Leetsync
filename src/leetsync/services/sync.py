# from leetsync.api.client import LeetCodeClient
# from leetsync.repository.manager import RepositoryManager

# class SyncService:
#     """Orchestrates the data extraction flow and channels items into the repo engine."""

#     def __init__(self, client: LeetCodeClient, repo_manager: RepositoryManager) -> None:
#         self.client = client
#         self.repo_manager = repo_manager

#     def run(self, username: str) -> None:
#         print(f"[*] Checking for updates for user: {username}...")
        
#         # Pull records using state registers managed by the RepositoryManager
#         new_submissions = self.client.get_recent_submissions(
#             username=username,
#             last_sync_timestamp=self.repo_manager.state["last_sync_timestamp"],
#             known_submission_ids=self.repo_manager.state["known_ids"]
#         )

#         if not new_submissions:
#             print("Repository status: up to date. No new entries found.")
#             return

#         print(f"[+] Found {len(new_submissions)} new or modified entries to sync.")
        
#         # Process from oldest to newest
#         for sub in reversed(new_submissions):
#             print(f"    -> Querying details for: {sub.title} (ID: {sub.id})")
#             details = self.client.get_submission_details(int(sub.id))
            
#             if details:
#                 # Local disk storage write operation
#                 saved_file = self.repo_manager.save_to_disk(sub.title_slug, details.code, details.language)
#                 commit_msg = f"Sync: {sub.title} ({details.language}) [id: {sub.id}]"
                
#                 # Only commit locally during the loop to avoid Git remote conflicts
#                 self.repo_manager.git_commit(saved_file, commit_msg)
                
#                 # Update tracking indices registers
#                 self.repo_manager.state["known_ids"].add(str(sub.id))
#                 if sub.timestamp > self.repo_manager.state["last_sync_timestamp"]:
#                     self.repo_manager.state["last_sync_timestamp"] = sub.timestamp

#         # Update tracking registry file locally
#         state_file_path = self.repo_manager.state_file
#         self.repo_manager.save_state()
#         self.repo_manager.git_commit(state_file_path, "Sync: update tracking state engine profile metadata")
        
#         # Push the entire batch cleanly at the very end
#         self.repo_manager.git_push()
#         print("Sync lifecycle complete.")
