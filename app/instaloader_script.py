import instaloader
from instaloader import Instaloader, Profile, exceptions

def format_number(number):
    if isinstance(number, float):
        return "{:,.2f}".format(number).replace(",", "X").replace(".", ",").replace("X", ".")
    return "{:,}".format(number).replace(",", ".")

def calculate_engagement(username):
    ig = Instaloader()
    try:
        ig.load_session_from_file('_txt.28', 'C:/Users/ACER/OneDrive/Desktop/Frontend IG/session-_txt.28') #Ganti direktori sesuai tempat session
    except Exception:
        return {"error": "Connection error occurred."}

    try:
        profile_import = Profile.from_username(ig.context, username)
        if profile_import.is_private:
            return {"error": "The account is private."}

        num_followers = profile_import.followers
        num_following = profile_import.followees

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

        engagement_formatted = format_number(round(engagement * 100, 2))
        avg_likes_per_post_formatted = format_number(round(avg_likes_per_post, 2))
        avg_comments_per_post_formatted = format_number(round(avg_comments_per_post, 2))

        return {
            "username": username,
            "engagement": engagement_formatted,
            "total_likes": format_number(total_num_likes),
            "total_comments": format_number(total_num_comments),
            "total_posts": format_number(total_num_posts),
            "avg_likes_per_post": avg_likes_per_post_formatted,
            "avg_comments_per_post": avg_comments_per_post_formatted,
            "followers": format_number(num_followers),
            "following": format_number(num_following)
        }

    except exceptions.ProfileNotExistsException:
        return {"error": "The username was not found."}
    except exceptions.PrivateProfileNotFollowedException:
        return {"error": "The account is private."}
    except ZeroDivisionError:
        return {"error": "Cannot calculate engagement due to zero division."}
    except exceptions.ConnectionException:
        return {"error": "Connection error occurred."}
    except exceptions.BadCredentialsException:
        return {"error": "Bad credentials."}
    except exceptions.LoginRequiredException:
        return {"error": "Login required."}
    except Exception as e:
        return {"error": str(e)}