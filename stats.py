def get_num_words(text):
    words = text.split()
    return len(words)

def get_chars_stats(text):
   stats = {}
   #text_lowecased = text.lower()
  
   for character in text.lower():
       if character in stats:
           stats[character] += 1
       else:
           stats[character] = 1

   return stats

def sort_stats(stats):
    sorting_list = []
    
    for entry in stats:
        sorting_list.append({"entry": entry, "num": stats[entry]})

    sorting_list.sort(reverse = True, key = sort_on_count)

    return sorting_list

def sort_on(stats: tuple[str, int]) -> int:
    return stats[1]

def sort_on_count(stats):
    return stats["num"]

def chars_dict_to_sorted_list(chars_dict: dict[str, int]) -> list[tuple[str, int]]:
    chars_list: list[tuple[str, int]] = []

    for char in chars_dict:
        chars_list.append((char, chars_dict[char]))

    return sorted(chars_list, reverse=True, key=sort_on)
