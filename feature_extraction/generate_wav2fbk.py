import os
import sys


# read the scp file
scpFile = sys.argv[1]
outFile = sys.argv[2]
featureType = sys.argv[3]

f=open(scpFile,"r")
lines=f.readlines()
f.close()



#/scratch/bdda/xyliu/SpeechOcean_Cantonese/convert/import/Cantonese_From_SpeechOcean/DATA/CHANNEL0/WAVE.mapped/SPCOCN-00006-GUANGZHO-XXXF23-an_FXX0000.WAV /project_bdda3/bdda/mengzhe/CUDYS_SpeechOcean_System/CUDYSC_Speechocean/dict_80/DATA/plp/SPCOCN-00006-GUANGZHO-XXXF23-an_FXX0000.plp

# read line by line
# /project/bdda/mengzhe/DataAugmentation/Data/UASpeech/UASpeech_trim/train/UASPCH-XCF02-XXB1CF02-UACF02-ih_CW100M2_0000027_0000104.wav
outLine = []


#/project/bdda/mengzhe/DataAugmentation/Data/UASpeech/1.1/UASPCH-XCM05-XXB1CM05-UACM05-ih_XXCW7M7_0000017_0000108.wav

for line in lines:
  line = line.strip()
  fileName = line.split("/")[-1].split("_")[0] + '_' + line.split("/")[-1].split("_")[1]

# sox command
# sox -t wav input.wav -t wav output.speed0.9.wav speed 0.9

# output the command to write clean labels
  outLine.append("%s /project/bdda/mengzhe/DataAugmentation/Data/UASpeech/%s/%s.fbk\n" % (line, featureType, fileName))


out_f = open(outFile, "w")

for line in outLine:
  out_f.write(line)

out_f.close()
