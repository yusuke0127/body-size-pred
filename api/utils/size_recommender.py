# Women's size
w_top_size_chart = [
    {"size": "XS", "bust": (74, 80), "waist": (57, 63), "height": (149, 156)},
    {"size": "S", "bust": (77, 83), "waist": (60, 66), "height": (153, 160)},
    {"size": "M", "bust": (80, 86), "waist": (63, 69), "height": (153, 160)},
    {"size": "L", "bust": (86, 92), "waist": (69, 75), "height": (159, 166)},
    {"size": "XL", "bust": (92, 98), "waist": (75, 81), "height": (159, 166)},
    {"size": "XXL", "bust": (98, 104), "waist": (81, 87), "height": (159, 166)},
    {"size": "3XL", "bust": (104, 110), "waist": (87, 93), "height": (159, 166)}

]

w_bottom_size_chart = [
    {"size": "XS", "waist": (57, 63), "hips": (82, 88), "height": (149, 156)},
    {"size": "S", "waist": (60, 66), "hips": (85, 91), "height": (153, 160)},
    {"size": "M", "waist": (63, 69), "hips": (88, 94), "height": (153, 160)},
    {"size": "L", "waist": (69, 75), "hips": (94, 100), "height": (159, 166)},
    {"size": "XL", "waist": (75, 81), "hips": (100, 106), "height": (159, 166)},
    {"size": "XXL", "waist": (81, 87), "hips": (106, 112), "height": (159, 166)},
    {"size": "3XL", "waist": (87, 93), "hips": (112, 118), "height": (159, 166)}
]

# Men's size
m_top_size_chart = [
    {"size": "XS", "bust": (78, 84), "waist": (66, 72), "height": (155, 165)},
    {"size": "S", "bust": (80, 88), "waist": (68, 76), "height": (155, 165)},
    {"size": "M", "bust": (88, 96), "waist": (76, 84), "height": (165, 175)},
    {"size": "L", "bust": (96, 104), "waist": (84, 92), "height": (175, 185)},
    {"size": "XL", "bust": (104, 112), "waist": (92, 100), "height": (175, 185)},
    {"size": "XXL", "bust": (112, 120), "waist": (100, 108), "height": (175, 185)},
    {"size": "3XL", "bust": (120, 128), "waist": (108, 116), "height": (175, 185)},
    {"size": "4XL", "bust": (128, 136), "waist": (116, 124), "height": (175, 185)}
]

m_bottom_size_chart = [
    {"size": "XS", "waist": (66, 72), "height": (155, 165)},
    {"size": "S", "waist": (68, 76), "height": (155, 165)},
    {"size": "M", "waist": (76, 84), "height": (165, 175)},
    {"size": "L", "waist": (84, 92), "height": (175, 185)},
    {"size": "XL", "waist": (92, 100), "height": (175, 185)},
    {"size": "XXL", "waist": (100, 108), "height": (175, 185)},
    {"size": "3XL", "waist": (108, 116), "height": (175, 185)},
    {"size": "4XL", "waist": (116, 124), "height": (175, 185)}
]


def in_range(value, range_tuple):
    return range_tuple[0] <= value <= range_tuple[1]


def size_recommender_top(bust_size, waist_size, height, gender):
    """
    Recommend top sizes based on bust, waist, height, and gender.
    
    Parameters:
    bust_size (int): Bust measurement
    waist_size (int): Waist measurement
    height (int): Height measurement
    gender (str): Gender ('F' for female, 'M' for male)
    
    Returns:
    list: Recommended top sizes
    """
    matching_sizes = []
    size_chart = w_top_size_chart if gender == "F" else m_top_size_chart
    for size in size_chart:
        score = 0
        if in_range(bust_size, size["bust"]):
            score += 1
        if in_range(waist_size, size["waist"]):
            score += 1
        if in_range(height, size["height"]):
            score += 1
        if score > 0:
            matching_sizes.append({"size": size["size"], "score": score})
    
    matching_sizes.sort(key=lambda x: x["score"], reverse=True)

    if matching_sizes:
        best_score = matching_sizes[0]["score"]
        best_matches = [size["size"] for size in matching_sizes if size["score"] == best_score]
        return best_matches
    
    return []
    

def size_recommender_bottom(waist_size, hip_size, height, gender):
    """
    Recommend bottom sizes based on waist, hips, height, and gender.
    
    Parameters:
    waist_size (int): Waist measurement
    hip_size (int): Hip measurement
    height (int): Height measurement
    gender (str): Gender ('F' for female, 'M' for male)
    
    Returns:
    list: Recommended bottom sizes
    """
    matching_sizes = []
    size_chart = w_bottom_size_chart if gender == "F" else m_bottom_size_chart
    for size in size_chart:
        score = 0
        if in_range(waist_size, size["waist"]):
            score += 1
        if "hips" in size and in_range(hip_size, size["hips"]):
            score += 1
        if in_range(height, size["height"]):
            score += 1
        if score > 0:
            matching_sizes.append({"size": size["size"], "score": score})
    
    matching_sizes.sort(key=lambda x: x["score"], reverse=True)

    if matching_sizes:
        best_score = matching_sizes[0]["score"]
        best_matches = [size["size"] for size in matching_sizes if size["score"] == best_score]
        return best_matches
    
    return []


def size_recommender(bust_size, waist_size, hip_size, height, gender):
    """
    Recommend top and bottom sizes based on measurements and gender.
    
    Parameters:
    bust_size (int): Bust measurement
    waist_size (int): Waist measurement
    hip_size (int): Hip measurement
    height (int): Height measurement
    gender (str): Gender ('F' for female, 'M' for male)
    
    Returns:
    dict: Recommended top and bottom sizes
    """
    top_sizes = size_recommender_top(bust_size, waist_size, height, gender)
    bottom_sizes = size_recommender_bottom(waist_size, hip_size, height, gender)
    
    return {
        "top_size": top_sizes,
        "bottom_size": bottom_sizes
    }

