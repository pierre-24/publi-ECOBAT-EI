all: main

main:
	python ./plot_EC.py ../data/EC_Ca_bare.csv ../data/EC_Ca_solv.csv \
	-n 'Ca$$_{(surf)}$$ + Ca$$_{(bulk)}$$ + 6 THF' 'Ca$$_{(surf)}$$ + Ca(THF)$$_6$$' \
	--zc 1200 --szc 1576 --limits=-4:0.0 -o ../Figure1.pdf
	
	python ./plot_EC2.py ../data/EC_Ca_bare.csv ../data/EC_Ca_solv.csv ../data/EC_Ca_2.csv  ../data/EC_Ca_3a1p.csv   ../data/EC_Ca_3b1.csv   ../data/EC_Ca_3a2p.csv   ../data/EC_Ca_3b2.csv    ../data/EC_Ca_3b3.csv \
	-n 'Bare' '$$\bf{1}$$' '$$\bf{2}$$' "$$\bf{3a_1{}'}$$" '$$\bf{3b_1}$$'  "$$\bf{3a_2{}'}$$" '$$\bf{3b_2}$$' '$$\bf{3b_3}$$' \
	--limits=-4:0.0 --left-limit=-4 -o ../Figure4.pdf
