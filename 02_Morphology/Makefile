all:
	hfst-lexc chv.lexc -o chv.lexc.hfst
	hfst-twolc chv.twol -o chv.twol.hfst
	hfst-compose-intersect -1 chv.lexc.hfst -2 chv.twol.hfst -o chv.gen.hfst
	hfst-lexc ava.lexc -o ava.lexc.hfst
	hfst-lexc fin.lexc -o fin.lexc.hfst
	hfst-invert chv.gen.hfst -o chv.mor.hfst
	echo "у р а м %<n%> ?*" | hfst-regexp2fst -o uram.hfst
	hfst-compose-intersect -2 chv.gen.hfst -1 uram.hfst | hfst-fst2strings
	cat noun-paradigm.txt | sed "s/^/у р а м /g"  | hfst-regexp2fst -j > uram.hfst
	hfst-compose-intersect -2 chv.gen.hfst -1 uram.hfst | hfst-fst2strings
	hfst-substitute -i chv.lexc.hfst -o chv.lexc_guesser.hfst  -f '🂡:🂡' -T chv.stem.hfst
	hfst-regexp2fst chv.restrict.regex -o chv.restrict.hfst
	hfst-invert chv.gen_guesser.hfst | hfst-compose -1 - -2 chv.restrict.hfst -o chv.mor_guesser.hfst
	hfst-compose-intersect -1 chv.lexc_guesser.hfst -2 chv.twol.hfst -o chv.gen_guesser.hfst
	hfst-regexp2fst chv.restrict.regex -o chv.restrict.hfst
	hfst-invert chv.gen_guesser.hfst | hfst-compose -1 - -2 chv.restrict.hfst -o chv.mor_guesser.hfst
	#cat chv.crp.txt  | sed 's/[^а-яӑӗăĕҫçА-ЯӐӖĂĔҪÇ]\+/ /g' | tr ' ' '\n' | sort -f | uniq -c | sort -gr  > chv.freq.txt
	cat chv.freq.txt | freq2prob.py | hfst-strings2fst -j -o chv.surweights.hfst
	echo "?::0" | hfst-regexp2fst | hfst-repeat | hfst-reweight -e -a 15.0 | hfst-minimise -o chv.maxweight.hfst
	hfst-union -1 chv.surweights.hfst -2 chv.maxweight.hfst -o chv.weights.hfst
	hfst-compose -1 chv.gen.hfst -2 chv.weights.hfst -o chv.gen_weighted.hfst
	# chv.symbols should be a file with a list of multicharacter symbols (e.g. <n>) specified one per line
	#cat chv.weights | hfst-strings2fst -j -m chv.symbols -o chv.strweights.hfst
	#echo "?::5.13579" | hfst-regexp2fst | hfst-repeat -o chv.maxweight.hfst
	#hfst-union -1 chv.strweights.hfst -2 chv.maxweight.hfst -o chv.weights.hfst


