import instaloader
from instaloader import Instaloader, Profile, exceptions

def calculate_engagement(username):
    ig = Instaloader()
    ig.load_session_from_file('_txt.28')

    try:
        profile_import = Profile.from_username(ig.context, username)
        if profile_import.is_private:
            return {"error": "The account is private."}

        num_followers = profile_import.followers

        total_num_likes = 0
        total_num_comments = 0
        total_num_posts = 0

        for post in profile_import.get_posts():
            total_num_likes += post.likes
            total_num_comments += post.comments
            total_num_posts += 1

        if num_followers == 0 or total_num_posts == 0:
            return {"error": "Cannot calculate engagement: either no followers or no posts."}

        engagement = float(total_num_likes + total_num_comments) / (num_followers * total_num_posts)
        avg_likes_per_post = total_num_likes / total_num_posts
        avg_comments_per_post = total_num_comments / total_num_posts

        engagement_formatted = round(engagement * 100, 2)
        avg_likes_per_post_formatted = round(avg_likes_per_post, 2)
        avg_comments_per_post_formatted = round(avg_comments_per_post, 2)

        return {
            "username": username,
            "engagement": engagement_formatted,
            "total_likes": total_num_likes,
            "total_comments": total_num_comments,
            "total_posts": total_num_posts,
            "avg_likes_per_post": avg_likes_per_post_formatted,
            "avg_comments_per_post": avg_comments_per_post_formatted
        }

    except exceptions.ProfileNotExistsException:
        return {"error": "The username was not found."}
    except exceptions.PrivateProfileNotFollowedException:
        return {"error": "The account is private."}
    except ZeroDivisionError:
        return {"error": "Cannot calculate engagement due to zero division."}
    except Exception as e:
        return {"error": str(e)}