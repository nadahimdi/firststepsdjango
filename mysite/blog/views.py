from django.shortcuts import render
from datetime import date
posts = [{
        "slug": "reading-books",
        "image": "books.jpg",
        "author": "nada",
        "date": date(2023, 4, 16),
        "title": "Favorite Books",
        "excerpt": "THE Books I chose ARE amazing",
        "content": "Books have always held a special place in human civilization, serving as gateways to knowledge, imagination, and inspiration. They possess the remarkable power to transport us to different worlds, eras, and perspectives, allowing us to experience the joys, sorrows, and triumphs of characters we have never met. Within the pages of a book, we can explore new ideas, expand our understanding of the world, and challenge our own beliefs. Whether it's a captivating novel, an insightful non-fiction work, or a thought-provoking piece of poetry, books have the ability to ignite our curiosity, ignite our emotions, and ignite our passion for learning. They provide solace during difficult times, companionship when we are alone, and enlightenment when we seek answers. With each turn of a page, we embark on a journey of discovery, gaining wisdom, empathy, and a deeper connection to the human experience. Books are timeless treasures, weaving stories and knowledge across generations, preserving the essence of humanity within their printed words. So, let us embrace the enchanting world of books, for within their boundless pages, we find not only stories, but a gateway to our own limitless potential."
    },
    {
        "slug": "playing-piano",
        "image": "piano.jpg",
        "author": "nada",
        "date": date(2021, 4, 16),
        "title": "Favorite Songs to Play",
        "excerpt": "THE songs I play ARE amazing",
        "content": "Playing the piano is a captivating and transformative experience that transcends mere musical notes. It is an artistic expression that allows one to communicate and connect with others on a profound level. The piano becomes an extension of oneself, as fingertips dance across the keys, evoking a symphony of emotions. From the gentle touch of a delicate melody to the thunderous power of a grand crescendo, the piano has the ability to convey a range of moods and stories. As a pianist, one discovers the harmonious blend of technique and expression, mastering the art of creating beauty through sound. The instrument becomes a sanctuary, a space where one can retreat and find solace, pouring heart and soul into each musical phrase. Through hours of practice and dedication, the piano becomes a faithful companion, offering a channel for self-discovery, personal growth, and creative exploration. Whether playing classical masterpieces, contemporary compositions, or improvising freely, the piano allows us to unlock our innermost emotions and share them with the world. It is a lifelong journey of discovery, continually challenging and inspiring us to reach new heights of musicality. Playing the piano is not just an act of making music, but a transformative experience that enriches the mind, touches the heart, and resonates with the very essence of our being."
    },
    {
        "slug": "baking",
        "image": "baking.jpg",
        "author": "nada",
        "date": date(2022, 4, 16),
        "title": "Favorite Cake I Baked",
        "excerpt": "The cakes I bake are amazing",
        "content": "Baking is a delightful art that combines science, creativity, and a sprinkle of magic. It is a culinary adventure that awakens the senses and fills the air with tantalizing aromas. From the moment ingredients come together, a symphony of flavors and textures begins to unfold. Mixing, measuring, and kneading doughs and batters, we embark on a journey of transformation. The oven becomes our portal to alchemy, as raw ingredients undergo a miraculous metamorphosis, emerging as golden crusts, fluffy cakes, and melt-in-your-mouth cookies. Baking is an act of patience and precision, where time and temperature hold the key to perfection. As we whisk, fold, and decorate, we infuse our creations with love and personal touch, turning simple ingredients into edible works of art. The process is both therapeutic and rewarding, as the aroma of freshly baked goods fills our homes and warms our hearts. But baking is not just about the end result; it's about the joy of sharing. From family gatherings to special occasions, the act of presenting a homemade treat brings people together, evoking smiles, laughter, and a sense of togetherness. Baking allows us to express our creativity, experiment with flavors, and celebrate the sweet moments in life. It is a reminder that with a pinch of flour, a dash of sugar, and a spoonful of passion, we can create something truly extraordinary."
    },
    {
        "slug": "travel-adventures",
        "image": "travel.jpg",
        "author": "nada",
        "date": date(2023, 6, 1),
        "title": "Memorable Travel Adventures",
        "excerpt": "Unforgettable experiences from my travels",
        "content": "Traveling and adventures hold the promise of exhilaration, discovery, and transformation. They beckon us to step outside our comfort zones and embrace the unknown. From exploring distant lands and immersing ourselves in vibrant cultures to embarking on thrilling escapades, each journey becomes a tapestry of unforgettable experiences. Travel opens our eyes to the vastness and diversity of the world, broadening our perspectives and deepening our understanding of humanity. It is in the midst of new landscapes, bustling streets, and breathtaking vistas that we find ourselves truly alive. Adventures stir our spirits, igniting a sense of wonder and pushing the boundaries of what we thought possible. Whether it's hiking rugged trails, diving into crystal-clear waters, or navigating bustling cityscapes, each adventure becomes a chapter in the story of our lives. They teach us resilience, foster personal growth, and create cherished memories that will last a lifetime. Traveling and adventures remind us that life is a grand expedition, and it is in venturing forth that we truly find ourselves."
    },
    {
        "slug": "photography-tips",
        "image": "camera.jpg",
        "author": "nada",
        "date": date(2023, 5, 15),
        "title": "Useful Photography Tips",
        "excerpt": "Enhance your photography skills with these tips",
        "content": "Photography is an art form that allows us to capture moments, tell stories, and express our unique perspectives. To enhance our photographic skills and create stunning images, a few essential tips can make all the difference. First and foremost, mastering composition is key. Understanding the rule of thirds, leading lines, and balance can help create visually engaging photographs. Additionally, paying attention to lighting is crucial. Whether it's the soft glow of golden hour or the dramatic shadows of harsh sunlight, utilizing light effectively can elevate the mood and atmosphere of our images. Another important aspect is exploring different angles and perspectives. By getting low, climbing high, or experimenting with unusual viewpoints, we can add depth and interest to our photographs. Furthermore, honing our patience and observation skills allows us to capture decisive moments and fleeting expressions. Being in tune with our surroundings and anticipating the right moment can result in captivating and impactful images. Lastly, post-processing techniques can enhance our photos further. From adjusting exposure and colors to applying creative filters and effects, editing can bring out the full potential of our images. With practice, an eye for detail, and a willingness to experiment, photography becomes a medium through which we can share our unique vision with the world."
    },
    {
        "slug": "healthy-lifestyle",
        "image": "fitness.jpg",
        "author": "nada",
        "date": date(2022, 8, 10),
        "title": " a Healthy Lifestyle",
        "excerpt": "Tips and advice for a balanced and healthy life",
        "content": "A healthy lifestyle is a harmonious balance of physical, mental, and emotional well-being, leading to a fulfilled and vibrant existence. It encompasses a holistic approach to self-care, focusing on nourishing the body, nurturing the mind, and fostering positive relationships. Central to a healthy lifestyle is regular physical activity, which not only strengthens our bodies but also boosts our energy levels and promotes mental clarity. Alongside exercise, maintaining a nutritious diet rich in whole foods, fruits, and vegetables provides essential nutrients that support overall health and vitality. Taking time for self-reflection, mindfulness, and stress management techniques allows us to cultivate inner peace, resilience, and emotional equilibrium. Prioritizing quality sleep and relaxation nurtures our bodies' restorative processes, ensuring optimal functioning and rejuvenation. Building and nurturing meaningful connections with others contributes to a sense of belonging, happiness, and social support. Embracing a healthy lifestyle is not about strict rules or deprivation but rather making sustainable choices that align with our individual needs and values. It empowers us to live life to the fullest, embracing joy, and embracing the journey towards well-being and fulfillment."
    },
    {
        "slug": "gardening-hacks",
        "image": "gardening.jpg",
        "author": "nada",
        "date": date(2022, 9, 25),
        "title": "Useful Gardening Hacks",
        "excerpt": "Make your gardening easier with these hacks",
        "content": "Gardening hacks are the secret tools and tricks that help both novice and experienced gardeners optimize their green spaces and cultivate thriving plants. These clever techniques can make gardening more efficient, effective, and enjoyable. One popular hack is companion planting, where specific plants are grown together to enhance growth and deter pests. For example, planting marigolds alongside vegetables can repel insects naturally. Another useful hack is creating homemade organic fertilizers and compost using kitchen scraps, which not only reduces waste but also provides nutrient-rich soil amendments. Additionally, vertical gardening allows for maximizing limited space by utilizing trellises, hanging baskets, or vertical planters, making it ideal for urban environments. Utilizing mulch around plants helps retain moisture, suppress weeds, and regulate soil temperature, reducing the need for frequent watering and weeding. To protect delicate seedlings from harsh weather conditions, placing clear plastic cups or cloches over them acts as mini-greenhouses, creating a microclimate for growth. Furthermore, using recycled materials such as old pallets, crates, or tires can be repurposed into unique and functional planters, adding a touch of creativity to the garden. Gardening hacks are valuable resources that empower gardeners to overcome challenges, save time, and achieve thriving, beautiful gardens."
    },
    {
        "slug": "art-inspiration",
        "image": "art.jpg",
        "author": "nada",
        "date": date(2023, 2, 5),
        "title": "Finding Inspiration in Art",
        "excerpt": "Exploring the world of art and its influence",
        "content": "Art is a profound expression of human creativity, imagination, and emotion that transcends boundaries and resonates with the soul. It encompasses a wide range of mediums, from painting and sculpture to music, literature, dance, and beyond. Art has the power to evoke deep feelings, provoke thought, and inspire change. It reflects the beauty, complexities, and diversity of the world we inhabit, offering new perspectives and challenging societal norms. Through art, artists delve into the depths of their inner worlds, bringing forth their unique visions and experiences to create works that captivate and engage viewers. It is a form of communication, a language that transcends words, allowing us to connect and understand one another on a profound level. Art invites us to contemplate, to question, and to appreciate the nuances of life. It can be a source of solace, healing, and personal growth, providing an outlet for self-expression and introspection. Art pushes boundaries, breaks conventions, and encourages us to think beyond the ordinary, fostering innovation and pushing the boundaries of human creativity. It is a testament to the power of human imagination and the boundless possibilities of the human spirit."
    }]


# Create your views here.
def get_date(post):
  return post["date"]
def principale(request):
  sorted_posts=sorted(posts, key=get_date)
  latest_posts=sorted_posts[-3:]
  return render(request, "blog/index.html",{"posts":latest_posts})
def blog(request):
  return render(request, "blog/posts.html",{"allposts":posts})
def blogdetails(request, slug):
    post = next((post for post in posts if post["slug"] == slug), None)
    return render(request, "blog/post-dtails.html", {"post": post})
