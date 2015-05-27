# wabr-python

*Web API Barcode Reader Server* &nbsp;(**[WABR](http://how-to.inliteresearch.com/web-api-barcode-reader/)**) offers a REST API for the Inlite Research [ClearImage Barcode Recognition](http://www.inliteresearch.com/barcode-recognition-sdk.php) technology.  
This `wabr-python` SDK  simplifies the WABR client-side Python development.<br>  Place `wabr.py`  from this repository into any folder in `PYTHON_PATH`.<br> 
Use sample code from `test.py` and `sample_code.py`
This SDK requires Python 2.6 or higher version.

### Create a Reader
```python
from wabr import  WAUtils, WABarcodeReader, WABarcode
WAUtils.SetStdoutUTF8()  # optionally enable non-ASCII barcode text and file names

reader = WABarcodeReader(serverUrl, authorization)
```
Where
+ `serverURL` is a WABR server URL 
	+ For customer-hosted server it is a URL address of your server
	+ For Inlite hosted server use empty string to send HTTP Request to `wabr.inliteresearch.com`.
+ `authorization` is a value set in `Authorization` field of HTTP Request header. If `authorization` is an empty string, then the value is set from the `WABR_AUTH` environmental variable (if present).
	+ For customer-hosted server: Use empty string if no authentication is required, otherwise use value expected by your IIS Authentication handler
	+ For Inlite-hosted server: Use *Authorization Code* supplied by Inlite.  Without a valid `authorization` value , the Test Server returns partial results which may be sufficient for testing your client-side code.  To obtain an Authorization Code contact Inlite at [sales@inliteresearch.com](mailto:sales@inliteresearch.com">sales@inliteresearch.com</a></span>).

### Read barcodes
Use the `Read()` method to obtain barcode values as an Array of `WABarcode` objects
```python
try:
   barcodes = reader.Read(image_source, types, directions, tbr_code)
   # Process barcode reading results
except:
   exc_type, exc_value, exc_traceback = sys.exc_info()
   WAUtils.printUTF8 ("EXCEPTION: " +  str(exc_value))  
``` 


Where
+ `image_source` is a required parameter to send an image(s) to WABR server. The following formats are accepted.
	- *URL* of Internet-based file. The name should start with `http://` , `https://` or `file://`.   Examples: 
```
https://wabr.inliteresearch.com/SampleImages/1d.pdf
http://upload.wikimedia.org/wikipedia/commons/0/07/Better_Sample_PDF417.png
```
	- *Path* of a file located on or accessible from the client.&nbsp;&nbsp;   Examples: 
```
c:/image_folder/some_image_file.tif
\\OBRSVR\another_folder\another_file.pdf
```
	- *Base64-encoded* string representing content of an image file.&nbsp;&nbsp;  Format:
	```
    [ data:[<MIME-type>][;base64],]<content>[:::<filename>]
    ```
<div style="margin-left: 4em;">
Example: 
```
data:application/pdf;base64,WTTVKM3OWFKFMERCMT5... :::IMAGE_FILE.PDF
```
The values in  **[ ]** are optional. The values in **< >** are variables. NOTE:  Neither **[ ]** nor  **< >** should be included in `image_source` string.<br>
`content` is the only *required* value. It is an image file content encoded as base64.<br>
`filename` is a value set to `WABarcode.File` element of each found barcode.  Default is an empty string.<br>
`MIME-type` identifies file format. I.e `application/pdf` or `image/tiff`.  Value is only for compatibility with data URI scheme.    Barcode reader will automatically identify file format based on content.
 </div>
 <BR>The most popular image formats are acceptable as image_source, including *PDF*, *TIF*, *JPEG* etc.  Multi-page *PDF* and *TIF* files are supported<br>
To specify several image sources in a single request separate them with ` | ` character. 
+ `types`  is an optional string parameter (*not case-sensitive*) that contains *comma-separated* barcode types to read.  An empty string is the same as `1d,2d`.  List of valid type is available in `WABarcodeReader.validtypes` variable.  Barcodes in this list are:

	`1d` - same as `Code39, Code128, Code93, Ucc128, Codabar, Interleaved2of5, Upca, Upce, Ean8, Ean13`<br>
	`Code39` - Code 39 Full ASCII<br>
	`Code128` - Code 128<br>
	`Code93` - Code 93<br>
	`Codabar` - Codabar<br>
	`Ucc128` - GS1-128<br>
	`Interleaved2of5` - Inteleaved 2 of 5<br>
	`Ean13` - EAN-13<br>
	`Ean8` - EAN-8<br>
	`Upca` - UPC-A<br>
	`Upce` - UPC-E<br>
	`2d` - same as `Pdf417, DatMatrix, QR`<br>
	`Pdf417` - PDF417 code<br>
	`DataMatrix` - DataMatrix code<br>
	`QR` - QR code<br>
	`DrvLic` - Driver License, ID Cards and military CAC ID<br>
	`postal` - same as `imb, bpo, aust, sing, postnet`<br>
	`imb` - US Post Intelligent Mail Barcode<br>
	`bpo` - UK Royal Mail barcode (RM4SCC)<br>
	`aust` - Australia Post barcode<br>
	`sing` - Singapore Post barcode <br>
	`postnet` - Postnet, Planet<br>
	`Code39basic` - Code 93 Basic<br>
	`Patch` - Patch code<br>

+ `directions`  is an optional string parameter to limit barcode recognition only to barcodes with specified orientation on a page.  Limiting direction can reduce reading time. Valid values are:

	*an empty string* - read barcode in any direction and skew angle. This is a *default* value.<br>
	`horz` - read only horizontal barcodes.<br>
	`vert` - read only vertical barcodes.<br>
	`horz, vert` - read only horizontal and vertical barcodes.<br>


+ `tbr_code` is an optional integer parameter supplied by Inlite to addresses *customer-specific requirements* for barcode recognition.  Read more about [*Targeted Barcode Reader (TBR)*](http://how-to.inliteresearch.com/barcode-reading-howto/tbr/).  Default value is 0, meaning *TBR* is disabled.

### Use barcode reading results

The following examples demonstrate processing of an Array of `WABarcode` objects returned by `Read()` method.  
Examples use `WAUtils.printUTF8` to correctly represent UTF8 character on `stdout`.

Print each barcode text value, type and file name: 
```python
for n in range(0, len(barcodes)):
   barcode = barcodes[n]
   print.printUTF8("Barcode Type:" + barcode.Type + "  File:" + barcode.File)
   WAUtils.printUTF8(barcode.Text)
``` 

Decodes `Values` of *Driver License*, *ID Card* or *Military CAC Card*. To get these values include `DrvLic` in the `types` parameter of the `Read()` call.  
```python
for key in barcode.Values:
    WAUtils.printUTF8 (key + ' : ' + barcode.Values[key])
``` 

#### `WABarcode` properties

`Text` - barcode text value (ASCII or UTF-8 if enabled) [string]<br>
`Data` - *binary data* encoded in `Pdf417`, `DataMatrix` or `QR` barcodes [array of bytes]<br>
`Type` - barcode type [string]<br>
`Page` - page in multi-page *PDF* and *TIF* file [integer]<br>
`Top` - top coordinate in pixels [integer]<br>
`Left` - left coordinate in pixels [integer]<br>
`Right` - right coordinate in pixels [integer]<br>
`Bottom` - bottom coordinate in pixels [integer]<br>
`File` - file name of image file.  Depending on `image_source` type it is <br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;a *URL* value, base-name of *Path*, `filename` of *Base64-encoded* string (if present) [string]<br>
`Rotation` - rotation of barcode on a page. Values: `none`, `upsideDown`, `left`, `right` or `diagonal` [string]<br>
`Meta` - XML formatted string representing barcode meta-data [string]<br>
`Values` - Driver License fields, such as last name, date of birth etc. [dictionary: key-field name string as key, value - field value string]<br>

#### Use UTF-8  notes
##### barcode `Text` and `File` values to `stdout`
 `Pdf417`, `DataMatrix` or `QR` barcodes can include language-specific text value.  If this you case, the `Text` variable contains UTF8 string.  Also `Read()` method accepts `image_source` as UTF8 string, resulting `File` variable also be UTF8.<br>
To represent UTF8 string on `stdout` use helper methods:
- `WAUtils.SetStdoutUTF8()` should be called once in your application.
- `WAUtils.printUTF8(string)` should be use to print UTF8 strings to `stdout`
