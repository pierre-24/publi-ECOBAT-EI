all: main SI

main:
	python ./plot_EC.py ../data/EC_Ca_bare.csv ../data/EC_Ca_solv.csv \
	-n 'Ca$$_{(surf)}$$ + 6 THF' 'Ca$$_{(surf)}$$ + Ca(THF)$$_6$$' \
	--zc 1200 --szc 1576 --limits=-4:0.0 -o ../Figure1.pdf
	
	python ./plot_EC2.py ../data/EC_Ca_bare.csv ../data/EC_Ca_solv.csv ../data/EC_Ca_2.csv  ../data/EC_Ca_3a1p.csv   ../data/EC_Ca_3b1.csv   ../data/EC_Ca_3a2p.csv   ../data/EC_Ca_3b2.csv    ../data/EC_Ca_3b3.csv \
	-n 'Bare' '$$\bf{1}$$' '$$\bf{2}$$' "$$\bf{3a_1{}'}$$" '$$\bf{3b_1}$$'  "$$\bf{3a_2{}'}$$" '$$\bf{3b_2}$$' '$$\bf{3b_3}$$' \
	--limits=-4:0.0 --left-limit=-4 -o ../Figure4.pdf
	
	python ./plot_q.py ../data/EC_Ca_solv.csv ../data/EC_Ca_2.csv  ../data/EC_Ca_3a1p.csv   ../data/EC_Ca_3b1.csv   ../data/EC_Ca_3a2p.csv   ../data/EC_Ca_3b2.csv    ../data/EC_Ca_3b3.csv \
	-n '$$\bf{1}$$' '$$\bf{2}$$' "$$\bf{3a_1{}'}$$" '$$\bf{3b_1}$$'  "$$\bf{3a_2{}'}$$" '$$\bf{3b_2}$$' '$$\bf{3b_3}$$' \
	--limits=-4:0.5 --zc=376 -o ../Figure5.pdf
	
	python ./plot_EC3.py ../data/EC_CaH2_bare.csv ../data/EC_CaH2_bare_ef.csv ../data/EC_CaH2_solv.csv ../data/EC_CaH2_3b1.csv \
	-n 'Bare (VB)' 'Bare (CB)' '$$\bf{1}$$' '$$\bf{3b_1}$$' \
	-c "C0" "lightblue" "C1" "C4" \
	-L -5 --limits="-4.5:2" -o ../Figure6.pdf

SI:
	python ./plot_wfunc.py `seq 45 55` 60 65 70 -o ../FigureS3.pdf
