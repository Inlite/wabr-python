from wabr import  WAUtils, WABarcodeReader , WABarcode

# This file should be saved with UTF8 encoding to Non-ASCII file names

class Test:
    samplesLocal = "./"
    samplesWeb = "https://wabr.inliteresearch.com/SampleImages/"

    
    bTestDropBox = True
    bTestSamplesLocal = True
    bTestSamplesWeb = True
    bTestBase64 = True
    bTestUtf8 = True
    bTestUtf8Names = True

    bShowBarcodes = True

    @staticmethod
    def Run(reader):
        
        # Read from image in DropBox
        if (Test.bTestDropBox):
            Test.Read(reader, "https://www.dropbox.com/s/qcd8zfdvckwwdem/img39.pdf?dl=1")

        # Read local files
        if (Test.bTestSamplesLocal):
            Test.Read(reader, Test.samplesLocal + "1d.pdf")

        # Read 1D barcodes and Read 2D barcodes in a single call
        if (Test.bTestSamplesWeb):
            Test.Read(reader, Test.samplesWeb + "1d.pdf" + " | " + Test.samplesWeb + "2d.pdf")

        # Read specifying types 
        if (Test.bTestSamplesWeb):
            Test.Read(reader, Test.samplesWeb + "postal.pdf", types="postal")

        # Read Driver License (TBR code)
        if (Test.bTestSamplesWeb):
            Test.Read(reader, Test.samplesWeb + "drvlic.ca.jpg", types="DrvLic")

        # Read from multi-page TIF file
        if (Test.bTestSamplesWeb):
            Test.Read(reader, Test.samplesWeb + "c39.multipage.tif")

        # Read specifying Target Barcode Reader (TBR code)
        if (Test.bTestSamplesWeb):
            Test.Read(reader, Test.samplesWeb + "I25.tbr132.jpg", tbr_code=132)

        # Read AdobeÃÂ® LiveCycleÃÂ® barcodes and decompress. (UTF-8 generates an error in print(barcode.Text))
        if (Test.bTestSamplesWeb):
            Test.Read(reader, Test.samplesWeb + "pdf417.adobe.pdf")

        # Read UTF8-encoded values (UTF-8 generates an error in print(barcode.Text))
        if (Test.bTestUtf8):
            Test.Read(reader, Test.samplesWeb + "pdf417.utf8.pdf")

        # Read from UTF8-named files
        if (Test.bTestUtf8Names):
            Test.Read(reader, Test.samplesWeb  + "pdf417.ЙшзщЪфг_Russian.pdf")
        if (Test.bTestUtf8Names):
            Test.Read(reader, Test.samplesWeb  + "pdf417.بساطة لأنه الأل_Arabic.pdf")


        # Read from Base64-encoded image content
        strBase64 = "SUkqAAgAAAANAP4ABAABAAAAAAAAAAABAwABAAAA1AIAAAEBAwABAAAAawEAAAIBAwABAAAAAQAAAAMBAwABAAAABAAAAAYBAwABAAAAAAAAABEBBAABAAAAvgAAABYBAwABAAAAawEAABcBBAABAAAAsBIAABoBBQABAAAArgAAABsBBQABAAAAtgAAACgBAwABAAAAAgAAADEBAgAtAAAAbhMAAAAAAAAAAAAALAEAAAEAAAAsAQAAAQAAAP/////lnFOWgJn2R85HGaM2KbCIOWUhGYzSOM2zjNiIGhadrfybgaIPNGcj2Tim2bENs2Immtpr3ffrJsoRhERHo0ZmwRFsnAdphBpp2mq3f/X/vLdIikjgpm4gzZppqmq///fXf///K75Qj5n40ZxmbNkEGfM2ad2n2t//69df////OwpFGejjMzNxozQ0RIBoGnad/+v+69/a/+/////yNZPHBTxHmbFNiBBoNB3p2v9//evv6vf1vvr+CKHfX///Qd2g1v/q/////f/33/q9f1x3//6/6drf60v//X//v////+7+1//7ev//77////////p++t76ftet+vw/X/X/f/v/q//9f9Vev/0/p/6761+0vX767/X33X/+/////fta//6f/V/f13///7/9ev6//+qf933v6a/u/6+////1/+/e/9L///fr1/a//3366/v/ruq/v61/t//fv/9P3q//f/////9f///7//r/pf+v2//6///uv//v/////3f6///1//3///X/331/////drr/f7bv7//r///7///36+//+63/9/1//3+tf/3////////611/1/9f+v/f//+l33/rvXv/+/f/p+7rX9ev/9/1v////9df//X/v/evv3/7/9f/+u31/+//rv/+v0/9Jr/19etfvf3//1/v/9/1X/f/S/v/+/v3v//9f/v//7/v/++//+r0/637//9fXf/1669X/19/v/6vf/Wv/1///7/v/997uv/7/1r/f9a3/vX9df/9f///rX//9ff/9rW/3v+/7//uv3+//////q96rrv/+3/3//3/X9v/X2///////3/v769//3//vvVa/r/9r77/W//t//1//f////XbXf9////X7//173+6/1S1///uuvf///9///ev+/9/+/7f9//9X9Wv/9f9r1//3/0utff10//r///v9f/v66ev370v+/v0v//////+/7tf/X33t3////9VdrX/+t/////1/+7/11qv///+/d73+////X33//9V/7q93/7/r/X/6f9//1+/r6fe97/7/9pr/19X77/+63/b/7///f9fX/X/6f//vvvV6/t6/pV/+//S/Xv27//dV//611r6r+kv/u//17//v0t9V9f07//+///7/vX1///X/X7/+/v9vX/3v/ve7rX9brf/7/9//9+t/7///91f9a1v+///e/X//+uq6f/+tU/7/uv//v//+/1//1//f/+/39b9f///0l///9b//+n3v/1r/X/dfr6f/+9vr/VfCKH/f/+7v/97fr/1fV//tf7+rrb/d71j/3X//r/+vev/+v3/+//V9a678b9e///f+/f7/3p3///1/71vb/+SHrr///116/vr/+9vb///+/df/r3f///1////76d1pdfX+/7//X67uu9f/+///X/13r//Xf1/9d6///+1/v//99P/7/f/v3r7/f693vt///31+t//v/f9Lvv/9/362nf6///+9r/3+/X//++q////+v///1//p76//////93/Xf//3/W/63vv99rT//3//X/+v///696fvX9/9fpd//7qv/q+//r9X/X/1V///16//rrf9X////3/+v7/3tPX/f/1f33++uqv/9d//r/3///T//6167//11/3//vf1/7f+///TT9//r3//tb9771/v1/9e/3/v1/a0///Df//9/1/31/3r/f//1/f+/X/+v/7//7////66//6+///9P9r3a/11/9///f/9+9df/+v/17/r/f/3/+re////3/+/9d//+/XXv/X//X//v///+//////v/79b9Prvv/71/////Xv/7v/99dbf+9e/f9d6/9a//r//7/9Vr//79a7/6///fqu/v/3///////W3rq99f//66/3v//9r/9rr/2/X//fr////+/r//9NX//9//+9v/6X7/v9f7ft16/rr1u/T//Xvr/XX/7/T//v/rv6//3/rX//1pd/77///tda9/fr197f/////+33////9/Xq/6r//rd/Sv/////3//6//br73//f//+v3//+//////f/9X9+/f6/3+/+63/////////6//QVf/7/1/++na//9f/r13/+v7/r27/X3/7//X3///3//v//r///1/v/6//9v9f/////9f/f/9b/1/fX3v/+l//+///3/////7///r+/X/6///1//7/Xf/7///73+v/+n/3fpf7///16+v/1/39f/9/6///rvb/X/6//f3///////r3/7X97+39f6733////X//el//+u//+v3/vf3pf//f/+7/6+2/39//////pf/3vr/3///X9/69uvq/6///XX//+13/6X1/+/6v/69/Xf9//e/7//1v7X+///X/f1v66//+v/f1//7//X///96/r///7fX/r31q9d/r9/99+tv/93+////67r/f/371//r/rr/X/1/7///+vX//9/1X///q/79b/7//1///////9d//6f/f/33X//+u//e3973f9/+3rf///6v6/v7/////6+tPf/66/ff/v//X/1/X////b6+/60/X/1r1/0v/33/+//X9//qv//fX+++1////+v//X/ve0vv/f/f9X9//76f/v/99d+//16//3177/06f/69/f977/39//9////X1/Vb/av/p/+vt///7a0uv/3/337//7/////X///+//99//9//p//fpb/1+/X7Xqv7766+//r/6X/632v+9L1v9V/7+n1///f/X9a+36/ff//37/+/v/3/rr7/+v7e/9f/a////frr+9f//3v/3/fb61tv//9///v//v/f/+//+6r33/vrt//6///9f/Xr//9f+tff+vvX+q7/////v/797//e+v3+6///9ff///r/r+///1/9f+tVVv/rr+9f/Xr/db9//f9fv+k/9fv6X/677Xa9f7fT+/616v1/X/fV/v3/vr731hFD+19+/ra+v73+v+//9//f3fa/uv3j/a//QT/+//W9rf9////X/dP///9P//YfX7r8Iof/p/////vT6//f33//f//2/rXx99666//X91uv///6+v6/6/71e/9//f//v9r97S//6Xf2v//+uu///1/7/X639/0/V/+7W+v4IqP/1+v/rf7/X/v9/X/v7r/9PXb/H/37///qv/v/f/136/b//p/f4W/////v3/1v/9f/9f76//v1/3r333f/+v///////r/qu//+vsua/X+l9//+vv/rrpf7+/1u/9f794X16/T/W/////1v3//S6v///3/9q73+//+v+/Tr////6f1/X/f6et3//9/6+/7Xv/t//1/D7/9/fXq/9319dV////6//+////6/67r6/hf////3//03//3///3//797/91v/+/+v+/1/r+vvX7r1f/2la9L/r1//3/a/1/+///7/V+//3pft/wu/7/1/7/p+/6/v//f7//+n/Xf5Q67/+//CX/v6/9+uv/vetd/7933/u3r9f7/Df/r7/vX/9fX7/Vda/+v6f/+/r3//frf3///fWv/vvr/+u///13X9f/+vq3//f7wih6S///r/+q//1fX/+v/v6r/h+tW+O27//vvrf/r/v/3r+79d6/rquv+q+rX/V/X/f/37+v3ferUL7W6av7trf/9+v9///1/fX/v/+7Qj9P2G++tX///2t+nX+Ov3f36+v8H+5EHKHJDwmE0NYRH9e70K////waav+iT9p////p4T19Y4YZHDxI3fjhen37tfr/8Ij4TCKHDQavbX/XX/+/2oL6ccUyTqL1D9+yI/X/T73oU4aFimCI6VrfuCLq9f+/Tv9PVuQj5CP3knq7/X/giP//quo8m8fD/8f9f/+nd/wrfr12tev/aHf/d+yMf7gmEUPCX9f3f/3/7/11+Hr//t/r9+031/WPf3f////XS//uCKf/7/////67///r/f7//9f9r139/X//v///vr/6//+v//3//uP0v6/1+609f+vfX9//////d/1/rT/3/39P////b/f/////f/9/+7+/f/9PffX3+//77/q/1/rX/r/9fX/1/9fv/9f9df/f+/77X/f/7+/X7+/v/9fhvv/r/+1/+vf//76//9/36//f4S//fX/V//3///////r6+//////f////+v///f1f+nv//3/v1///r9X9e///////99df/rf1t//r//vvv177ff//99/1vb//6+/en/f//9f9f0v/2v///1r9f//qv7//fuq/+//1////+u9/v+7/+9LXr/////Xv+/X/6/31+//Vf9Pd0/e/+v////+/671/6/XX/+vvr9f//r///6//fa1v399///9/X/b/r////7779f1f7/6ev6///7v9f33+/9f/VPtdfv2////39//X/7/rr7/79+r+vf/3WtfbX//qv++v////e//99+v+/rp/uvf//f//X/+//XW/v1///9fff6//v97/9f/9fXT//r//9/7/X6//6Xev/tu//+wt9/1vXv/vr/+/1vb+/v///2rv/4///X/9dPr/6W3v+61/63/r69f6yY7//9///ff/7/r//9P//9L1/W3g///+/+//6v10v717//r/f//+uv////+/T9tb3//7//9/+3X/3//X3/////11rvv////7/q3v/7/7+v///9//v/X7rW99v/v2/////3///X///X+3pd/X/3rXS+v///Wv1////7//63/e/10v+/////v/9r/fX//d/66//11v/9f//v/vv3p/6//6/e+/v9fv9f+r3f/9f////339f///f/1/7//qv///+/////X/r6/36////7d+////dd/f9/+3///9ff/7/X19f/6/+rqv/6/+v//9/r/6//719f//9f3+v/////f//v/3//9//7fvuu61p/v67/3/r//+/6+2/r+v/91/9//1/1f/v/X/6933rVPv//+v//9/+33//XX+++/eq/+1T0///dr//X//X////fr/33+vf/+7f/+v/v///+//36///r+tr/+l/9d///a/+vf///+//S3+3//9//67//6b/99evr///6//////r/3///1///f3b///3////Xv//////v/td+v///6/t661//9e//+v/199+/9/6/3/a/r//bX9b9P/33+9/r/r/////6//769N77X////1r6//6X/0/////3/+v7/r//v1/t/r/v/7W/a/t/r6+/3//v/69e/9XXf+///6p/0v/f79a/+6T/9//+/v/////f/3/96/3bd//336/ff//X+v/163/3/v9/+uv0r/q/+v/uv////6f///9a17Wq/3vX1v///f////v9f/9f//+v9r9//3/f6//2v/1v///+u/9+//fp/r/pa7V//9//f/+v//fv1//ul2v/7/9P/7////vvv+9f/7V2v/vf/9rv//b///f//W/+73X/te7+tdPXf+//+k/9f///v///d/7u//tfb//3///r////+ut/7r/r+v/pqrv6f//73+//vf/99/Xf7rr//96f////9af6//r//3+/7SV+9e/vre+v1////ve/6///1/17vf/9/9r99///T3/Vdd9//f3T+vpq/tr1/7//6/Xf7X///6//+v/3rS+n/1f3/69++v//3d3/f/9f/v7f1rXf/pf//////1//rvX7+7//d7Vu+vr2//97///9bVV/319//1+tL71/9963/+l////7v1/v0v/r///6/363r/9v///33//33/66d/////X9f//X///+r//+n/+n//9+/+/17///3///1Xv9fvXv/+/9f99e7fX//+u//+////7/6r///+tPrp////b//1//X9erW9NMJ/66/r/f11////////X1W7TTCFhCIiP/tvfv/X///9/+v6+mqaoRDPJK/vrT69////6pf92qac+i6DCERERr//X+u+//9Pu00wmClRYQiIiI3/133ffpqnaaaYQtMEIiIiIj/reuumqYTCKEIiIiI96doGEGCYTQiIiI2EIiIiIx//JuLMqxZNkiI+CBhBy3OKhJGQMJwQeCaDgg9NOgfpwnaadOvhPX32iFt75DvoPCIL36f6BBsqizqJXXhBzqEIMTTBr706DQwgYa9vWCahMUtfUNU+/sEFTsEuqjaqla6QaSaUMJ9ZCZkJjdiuiHvh0nT/Ta9PDfpN0/bv6dLsxhW29b+hGDb7/93//th+v35LheU7r/d9oN/8lxdLw0/9czHW7fvkLBQm1C9wul7jra77V14aS+19vzQ44qwYSbW1tEIIT2O0tWN+0xx9NaadoNNXp2mqtNO1TChhU7QaatBhbBBhAwrCaBkXIMIM7lNy0GgYQiIjBlMlB//////ABABSW5saXRlIFJlc2VhcmNoLCBJbmMuIFRpZmYgV3JpdGVyIDIuMDAuMDAuMDAA"
        if (Test.bTestBase64):
            Test.Read(reader, strBase64)

        #  Read from Base64-encoded local image file
        if (Test.bTestBase64):
            Test.ReadFileBase64(reader, Test.samplesLocal + "2d.pdf")

        

    @staticmethod
    def ReadFileBase64(reader, file):
        try:
            strBase64  = WAUtils.fileToBase64(file)
            Test.Read(reader, strBase64)
        except:
           exc_type, exc_value, exc_traceback = sys.exc_info()
           WAUtils.printUTF8 ("EXCEPTION: " +  str(exc_value))     
           if (image != ""): WAUtils.printUTF8 ("  processing: " + WAUtils.signature(image))





    @staticmethod
    def ShowBarcodes(barcodes):
        if (Test.bShowBarcodes == False): return
        for n in range(0, len(barcodes)):
            barcode = barcodes[n]
            print("")
            WAUtils.printUTF8("Barcode Type:" + barcode.Type + "  File:" + barcode.File + "   Page:" + str(barcode.Page))
            WAUtils.printUTF8(barcode.Text)
            if (len(barcode.Values) > 0):
                print ("VALUES:")
                for key in barcode.Values:
                  WAUtils.printUTF8 (key + ' : ' + barcode.Values[key])
    
    @staticmethod
    def ShowException (image):
       exc_type, exc_value, exc_traceback = sys.exc_info()
       WAUtils.printUTF8 ("EXCEPTION: " +  str(exc_value))     # the exception instance
       if (image != ""): WAUtils.printUTF8 ("  processing: " + WAUtils.signature(image))


    @staticmethod
    def Read(reader, image, types="", directions="", tbr_code=0):
       try:
           barcodes = reader.Read(image, types=types, directions=directions, tbr_code=tbr_code)
           Test.ShowBarcodes(barcodes)
       except:
           exc_type, exc_value, exc_traceback = sys.exc_info()
           WAUtils.printUTF8 ("EXCEPTION: " +  str(exc_value))    
           if (image != ""): WAUtils.printUTF8 ("  processing: " + WAUtils.signature(image))
