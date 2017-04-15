
for i in {0..3000}
do
	OUTPUT="$(echo $i | nc shell2017.picoctf.com 57641)"
	if [[ $OUTPUT == *"Let's see if it was right"* ]]; then
		echo "$i = nope"
	elif [[ $OUTPUT == *"Congratulations"* ]]; then
		echo "$i = success"
		exit 1
	fi
done