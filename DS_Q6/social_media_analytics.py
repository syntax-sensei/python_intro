from collections import Counter, defaultdict

posts = [
{"id": 1, "user": "alice", "content": "Love Python programming!", "likes": 15, "tags": ["python", "coding"]},
{"id": 2, "user": "bob", "content": "Great weather today", "likes": 8, "tags": ["weather", "life"]},
{"id": 3, "user": "alice", "content": "Data structures are fun", "likes": 22, "tags": ["python", "learning"]},]

users = {
"alice": {"followers": 150, "following": 75},
"bob": {"followers": 89, "following": 120},}

tags = []

for i in range (0, len(posts)):
    x = posts[i]["tags"]
    tags.append(x)

#flatten 2d to 1d array    
flat = sum(tags, [])

# Count occurence of each element    
ctr = Counter(flat)

# Calculate the most common element
mc = ctr.most_common(1)

print(f"The most frequent tag is \"{mc[0][0]}\", it occurs \"{mc[0][1]}\" times")

print("\n")

total_likes = defaultdict(int)

for post in posts:
    user = post["user"]
    likes = post["likes"]
    total_likes[user] += likes

for user, likes in total_likes.items():
    print(f"{user} has {likes} total likes.")

print("\n")

top_posts = sorted(posts, key=lambda post: post["likes"], reverse=True)

print("📊 Top Posts by Likes:")
for post in top_posts:
    print(f"- {post["user"]} | Likes: {post["likes"]} | \"{post["content"]}\"")
