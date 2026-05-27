items = {
    "python for Beginners": ["python","programming", "Basics"],
    "Machine Learning Course": [
        "python",
        "ai",
        "machine learning",
        "data"],
    "Web Development Bootcamp": [
        "html",
        "css",
        "javascript",
        "web"
    ],
    "Deep Learning Fundamentals": [
        "python",
        "ai",
        "deep learning",
        "neural networks"
    ],

    "Data Science Essentials": [
        "python",
        "data",
        "analysis",
        "statistics"
    ]
}
print("Enter your interests separated by comma")
print("Example: python, ai, data")
user_input=input("Your interests: ")
user_preferences = user_input.lower().split(",")
#ازاله المسافات
user_preferences = [item.strip() for item in user_preferences]

def jaccard_similarity(user_tags, item_tags):

    # تحويل القوائم إلى Sets
    set_user = set(user_tags)
    set_item = set(item_tags)

    # التقاطع
    intersection = set_user.intersection(set_item)

    # الاتحاد
    union = set_user.union(set_item)

    # حساب التشابه
    similarity = len(intersection) / len(union)

    return similarity

#حساب التشابه لكل عنصر
recommendations = []

for item_name, item_tags in items.items():

    similarity_score = jaccard_similarity(
        user_preferences,
        item_tags
    )

    recommendations.append(
        (item_name, similarity_score)
    )

#ترتيب النتائج
recommendations.sort(
    key=lambda x: x[1],
    reverse=True
)
print("\n===== Recommended Items =====\n")

for item, score in recommendations:

    # عرض العناصر التي لديها تشابه فقط
    if score > 0:

        print(f"{item} --> Similarity Score: {score:.2f}")