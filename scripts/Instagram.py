from curl_cffi import requests
import json
import random

class SearchInsta:
    def __init__(self , username , timeout:float=random.uniform(0.1 , 5)):
        self.username = username
        self.timeout = timeout
       # impersonate 'chrome' with the following headers
        self.headers = {
                "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
                "x-ig-app-id": "936619743392459"
        }

        # what labels to look-for
        self.labels: dict = {
            "followed_by_viewer": "Followed by you",
            "edge_follow": "Following Count",
            "follows_viewer": "Follows you",
            "full_name": "Full Name",
            "group_metadata": "Group Metadata",
            "has_ar_effects": "Has AR Effects",
            "has_clips": "Has Reels/Clips",
            "has_guides": "Has Guides",
            "has_channel": "Has Broadcast Channel",
            "has_blocked_viewer": "Blocked You",
            "highlight_reel_count": "Story Highlights Count",
            "has_onboarded_to_text_post_app": "Threads App User",
            "has_requested_viewer": "Requested to Follow You",
            "hide_like_and_view_counts": "Hiding Likes/Views",
            "id": "Internal User ID",
            "is_business_account": "Is Business Account",
            "is_professional_account": "Is Professional Account",
            "is_supervision_enabled": "Parental Supervision On",
            "is_guardian_of_viewer": "Is Your Guardian",
            "is_supervised_by_viewer": "Supervised by You",
            "is_supervised_user": "Is Supervised Account",
            "is_embeds_disabled": "Embeds Disabled",
            "is_joined_recently": "Account Created Recently",
            "guardian_id": "Guardian ID",
            "business_address_json": "Business Address",
            "business_contact_method": "Contact Method",
            "business_email": "Public Email",
            "business_phone_number": "Public Phone",
            "business_category_name": "Business Niche",
            "overall_category_name": "Main Category",
            "category_enum": "Category Enum",
            "category_name": "Category Name",
            "is_private": "Is Private Account",
            "is_verified": "Is Verified (Blue Check)",
            "is_verified_by_mv4b": "Verified via Meta Verified",
            "is_regulated_c18": "Age Regulated Content",
            "edge_mutual_followed_by": "Mutual Followers"

            }

        # call the scraping logic at the end
        self.scrape()

    def scrape(self):
            try:
                url = f"https://www.instagram.com/api/v1/users/web_profile_info/?username={self.username}"
                result = requests.get(url , timeout=self.timeout , headers=self.headers , impersonate="chrome")

                print(f"({result.status_code}) probed: \033[33m{url}\033[0m")

                if result.status_code == 200:
                    user_data = result.json()["data"]["user"]

                    for key, value in user_data.items():
                        # Only process keys we defined in our label map
                        if key in self.labels:
                            describer = labels[key]
                            if isinstance(value, dict) and "count" in value:
                                clean_value = f"{value['count']:,}"
                            else:
                                clean_value = value
                            print(f"{describer}: {clean_value}")

                else:
                    print(f"({result.status_code}) @{self.username} is unreachable")


            except Exception as e:
                print(f"[\033[31merror\033[0m] @\033[33m{self.username}\033[0m raised  {e}")
