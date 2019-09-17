
## Count word initial consonant sequences.

# tokenise by word
sed 's/[^a-zA-Z]\+/\n/g' > $$words

# get words that start with consonants
grep -i '^[^aeiou].*$' $$words |

# delete the vowels and the rest of the word, sort and count
sed 's/\([aeiouAEIOU].*\)//' | sort > $$consonants

# count unique instances of consonant words
uniq -c < $$consonants

