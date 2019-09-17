
## Count word final consonant sequences

# tokenise by word
sed 's/[^a-zA-Z]\+/\n/g' | rev > $$revwords

# get words that start with consonants
grep -i '^[^aeiou].*$' $$revwords |

	# find the first vowel of a word and delete from that onwards
sed 's/\([aeiouAEIOU].*\)//' | rev | sort > $$revconsonants

# sort and count unique instances of initial consonant clusters
uniq -c < $$revconsonants
