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

def sort_on_count(stats):
    return stats["num"]
