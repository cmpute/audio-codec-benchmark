# Criteria
- *Compression Ratio (CR)*: compressed file size / original uncompressed file size (lower the better)
- *Spectrogram Error*: direct difference between power spectrograms (lower the better)
- *Weighted Spectrogram Error*: direct difference between A-weighted power spectrograms (lower the better)
- *Signal-to-Noise Ratio (SNR)*: noise is calculated from signal power difference (higher the better)
- *Weighted SNR*: noise is calculated from A-weighted signal power difference (higher the better)
# Results for `PLight - Bass_tek 2.wav`
Audio Format: 2ch, 16-bit, 44100 Hz, 10295292 samples
<table><tr><th rowspan="2">Format</th><th rowspan="2">Codec</th><th rowspan="2">Compression Ratio (%)</th><th rowspan="2">Encoding time (s)</th><th rowspan="2">Decoding time (s)</th><th colspan="2">Spectrogram Error (db)</th><th colspan="2">Signal-to-Noise Ratio (db)</th></tr>
<tr><th>linear</th><th>weighted</th><th>linear</th><th>weighted</th></tr>
<tr><td colspan="9" style="text-align:center"> Lossless Codecs </td></tr>
<tr><td rowspan="3">optimFrog</td><td>ofr (--preset 0)</td><td>78.722</td><td>4.439</td><td>4.139</td><td>-</td><td>-</td><td>-</td><td>-</td></tr>
<tr><td>ofr (--preset 5)</td><td>77.700</td><td>12.016</td><td>8.817</td><td>-</td><td>-</td><td>-</td><td>-</td></tr>
<tr><td>ofr (--preset 10)</td><td>77.104</td><td>41.960</td><td>23.692</td><td>-</td><td>-</td><td>-</td><td>-</td></tr>
<tr><td rowspan="8">flac</td><td>flac (-0)</td><td>82.658</td><td>0.474</td><td>0.368</td><td>-</td><td>-</td><td>-</td><td>-</td></tr>
<tr><td>flac (-1)</td><td>80.941</td><td>0.469</td><td>0.374</td><td>-</td><td>-</td><td>-</td><td>-</td></tr>
<tr><td>flac (-2)</td><td>80.820</td><td>0.516</td><td>0.379</td><td>-</td><td>-</td><td>-</td><td>-</td></tr>
<tr><td>flac (-3)</td><td>80.620</td><td>0.470</td><td>0.395</td><td>-</td><td>-</td><td>-</td><td>-</td></tr>
<tr><td>flac (-4)</td><td>78.556</td><td>0.512</td><td>0.386</td><td>-</td><td>-</td><td>-</td><td>-</td></tr>
<tr><td>flac (-5)</td><td>78.503</td><td>0.593</td><td>0.386</td><td>-</td><td>-</td><td>-</td><td>-</td></tr>
<tr><td>flac (-6)</td><td>78.433</td><td>0.809</td><td>0.385</td><td>-</td><td>-</td><td>-</td><td>-</td></tr>
<tr><td>flac (-7)</td><td>78.314</td><td>0.963</td><td>0.391</td><td>-</td><td>-</td><td>-</td><td>-</td></tr>
<tr><td rowspan="5">ape</td><td>mac (-c1000)</td><td>79.469</td><td>2.407</td><td>2.926</td><td>-</td><td>-</td><td>-</td><td>-</td></tr>
<tr><td>mac (-c2000)</td><td>78.663</td><td>3.204</td><td>3.863</td><td>-</td><td>-</td><td>-</td><td>-</td></tr>
<tr><td>mac (-c3000)</td><td>78.380</td><td>3.371</td><td>4.052</td><td>-</td><td>-</td><td>-</td><td>-</td></tr>
<tr><td>mac (-c4000)</td><td>78.062</td><td>4.747</td><td>5.735</td><td>-</td><td>-</td><td>-</td><td>-</td></tr>
<tr><td>mac (-c5000)</td><td>77.753</td><td>9.835</td><td>10.870</td><td>-</td><td>-</td><td>-</td><td>-</td></tr>
<tr><td rowspan="6">wavpack</td><td>wavpack (-f)</td><td>80.767</td><td>0.821</td><td>0.726</td><td>-</td><td>-</td><td>-</td><td>-</td></tr>
<tr><td>wavpack (default)</td><td>79.851</td><td>0.970</td><td>0.829</td><td>-</td><td>-</td><td>-</td><td>-</td></tr>
<tr><td>wavpack (-h)</td><td>79.412</td><td>1.176</td><td>1.006</td><td>-</td><td>-</td><td>-</td><td>-</td></tr>
<tr><td>wavpack (-hh)</td><td>79.203</td><td>1.417</td><td>1.133</td><td>-</td><td>-</td><td>-</td><td>-</td></tr>
<tr><td>wavpack (-h -x1)</td><td>79.240</td><td>1.866</td><td>0.963</td><td>-</td><td>-</td><td>-</td><td>-</td></tr>
<tr><td>wavpack (-hh -x3)</td><td>79.023</td><td>7.673</td><td>1.145</td><td>-</td><td>-</td><td>-</td><td>-</td></tr>
<tr><td rowspan="4">wavpack(hybrid)</td><td>wavpack (-c -b192 -f)</td><td>82.059</td><td>1.852</td><td>1.258</td><td>-</td><td>-</td><td>-</td><td>-</td></tr>
<tr><td>wavpack (-c -b192)</td><td>81.477</td><td>2.079</td><td>1.473</td><td>-</td><td>-</td><td>-</td><td>-</td></tr>
<tr><td>wavpack (-c -b192 -h)</td><td>81.331</td><td>2.737</td><td>1.789</td><td>-</td><td>-</td><td>-</td><td>-</td></tr>
<tr><td>wavpack (-c -b192 -hh)</td><td>81.219</td><td>3.095</td><td>2.028</td><td>-</td><td>-</td><td>-</td><td>-</td></tr>
<tr><td rowspan="30">tak</td><td>takc (-p0 -tn1)</td><td>79.910</td><td>0.375</td><td>0.442</td><td>-</td><td>-</td><td>-</td><td>-</td></tr>
<tr><td>takc (-p0 -tn4)</td><td>79.910</td><td>0.206</td><td>0.454</td><td>-</td><td>-</td><td>-</td><td>-</td></tr>
<tr><td>takc (-p0e -tn1)</td><td>79.570</td><td>0.479</td><td>0.443</td><td>-</td><td>-</td><td>-</td><td>-</td></tr>
<tr><td>takc (-p0e -tn4)</td><td>79.570</td><td>0.198</td><td>0.443</td><td>-</td><td>-</td><td>-</td><td>-</td></tr>
<tr><td>takc (-p0m -tn1)</td><td>79.470</td><td>0.738</td><td>0.439</td><td>-</td><td>-</td><td>-</td><td>-</td></tr>
<tr><td>takc (-p0m -tn4)</td><td>79.470</td><td>0.220</td><td>0.439</td><td>-</td><td>-</td><td>-</td><td>-</td></tr>
<tr><td>takc (-p1 -tn1)</td><td>79.107</td><td>0.445</td><td>0.441</td><td>-</td><td>-</td><td>-</td><td>-</td></tr>
<tr><td>takc (-p1 -tn4)</td><td>79.107</td><td>0.195</td><td>0.445</td><td>-</td><td>-</td><td>-</td><td>-</td></tr>
<tr><td>takc (-p1e -tn1)</td><td>79.001</td><td>0.677</td><td>0.444</td><td>-</td><td>-</td><td>-</td><td>-</td></tr>
<tr><td>takc (-p1e -tn4)</td><td>79.001</td><td>0.205</td><td>0.443</td><td>-</td><td>-</td><td>-</td><td>-</td></tr>
<tr><td>takc (-p1m -tn1)</td><td>78.920</td><td>1.017</td><td>0.444</td><td>-</td><td>-</td><td>-</td><td>-</td></tr>
<tr><td>takc (-p1m -tn4)</td><td>78.920</td><td>0.311</td><td>0.444</td><td>-</td><td>-</td><td>-</td><td>-</td></tr>
<tr><td>takc (-p2 -tn1)</td><td>78.723</td><td>0.567</td><td>0.493</td><td>-</td><td>-</td><td>-</td><td>-</td></tr>
<tr><td>takc (-p2 -tn4)</td><td>78.723</td><td>0.193</td><td>0.504</td><td>-</td><td>-</td><td>-</td><td>-</td></tr>
<tr><td>takc (-p2e -tn1)</td><td>78.627</td><td>0.963</td><td>0.495</td><td>-</td><td>-</td><td>-</td><td>-</td></tr>
<tr><td>takc (-p2e -tn4)</td><td>78.627</td><td>0.267</td><td>0.499</td><td>-</td><td>-</td><td>-</td><td>-</td></tr>
<tr><td>takc (-p2m -tn1)</td><td>78.555</td><td>1.627</td><td>0.498</td><td>-</td><td>-</td><td>-</td><td>-</td></tr>
<tr><td>takc (-p2m -tn4)</td><td>78.555</td><td>0.458</td><td>0.500</td><td>-</td><td>-</td><td>-</td><td>-</td></tr>
<tr><td>takc (-p3 -tn1)</td><td>78.424</td><td>1.058</td><td>0.522</td><td>-</td><td>-</td><td>-</td><td>-</td></tr>
<tr><td>takc (-p3 -tn4)</td><td>78.424</td><td>0.300</td><td>0.517</td><td>-</td><td>-</td><td>-</td><td>-</td></tr>
<tr><td>takc (-p3e -tn1)</td><td>78.388</td><td>1.302</td><td>0.520</td><td>-</td><td>-</td><td>-</td><td>-</td></tr>
<tr><td>takc (-p3e -tn4)</td><td>78.388</td><td>0.360</td><td>0.525</td><td>-</td><td>-</td><td>-</td><td>-</td></tr>
<tr><td>takc (-p3m -tn1)</td><td>78.346</td><td>2.500</td><td>0.512</td><td>-</td><td>-</td><td>-</td><td>-</td></tr>
<tr><td>takc (-p3m -tn4)</td><td>78.346</td><td>0.695</td><td>0.528</td><td>-</td><td>-</td><td>-</td><td>-</td></tr>
<tr><td>takc (-p4 -tn1)</td><td>78.321</td><td>1.624</td><td>0.544</td><td>-</td><td>-</td><td>-</td><td>-</td></tr>
<tr><td>takc (-p4 -tn4)</td><td>78.321</td><td>0.440</td><td>0.553</td><td>-</td><td>-</td><td>-</td><td>-</td></tr>
<tr><td>takc (-p4e -tn1)</td><td>78.296</td><td>1.882</td><td>0.547</td><td>-</td><td>-</td><td>-</td><td>-</td></tr>
<tr><td>takc (-p4e -tn4)</td><td>78.296</td><td>0.504</td><td>0.551</td><td>-</td><td>-</td><td>-</td><td>-</td></tr>
<tr><td>takc (-p4m -tn1)</td><td>78.261</td><td>3.863</td><td>0.559</td><td>-</td><td>-</td><td>-</td><td>-</td></tr>
<tr><td>takc (-p4m -tn4)</td><td>78.261</td><td>1.053</td><td>0.554</td><td>-</td><td>-</td><td>-</td><td>-</td></tr>
<tr><td rowspan="1">tta</td><td>tta (default)</td><td>78.420</td><td>0.823</td><td>0.871</td><td>-</td><td>-</td><td>-</td><td>-</td></tr>
<tr><td rowspan="1">wma</td><td>wmaencode (-c lsl)</td><td>79.115</td><td>2.046</td><td>1.162</td><td>-</td><td>-</td><td>-</td><td>-</td></tr>
<tr><td rowspan="12">lossyflac(hybrid)</td><td>lossyflac (-q I -C|-1)</td><td>91.890</td><td>17.335</td><td>2.115</td><td>-</td><td>-</td><td>-</td><td>-</td></tr>
<tr><td>lossyflac (-q I -C|-4)</td><td>89.925</td><td>17.555</td><td>2.159</td><td>-</td><td>-</td><td>-</td><td>-</td></tr>
<tr><td>lossyflac (-q I -C|-7)</td><td>86.141</td><td>19.365</td><td>2.174</td><td>-</td><td>-</td><td>-</td><td>-</td></tr>
<tr><td>lossyflac (-q H -C|-1)</td><td>91.709</td><td>17.634</td><td>2.123</td><td>-</td><td>-</td><td>-</td><td>-</td></tr>
<tr><td>lossyflac (-q H -C|-4)</td><td>89.745</td><td>17.819</td><td>2.238</td><td>-</td><td>-</td><td>-</td><td>-</td></tr>
<tr><td>lossyflac (-q H -C|-7)</td><td>86.359</td><td>19.729</td><td>2.182</td><td>-</td><td>-</td><td>-</td><td>-</td></tr>
<tr><td>lossyflac (-q S -C|-1)</td><td>91.661</td><td>17.762</td><td>2.131</td><td>-</td><td>-</td><td>-</td><td>-</td></tr>
<tr><td>lossyflac (-q S -C|-4)</td><td>89.721</td><td>17.819</td><td>2.186</td><td>-</td><td>-</td><td>-</td><td>-</td></tr>
<tr><td>lossyflac (-q S -C|-7)</td><td>86.466</td><td>19.752</td><td>2.183</td><td>-</td><td>-</td><td>-</td><td>-</td></tr>
<tr><td>lossyflac (-q X -C|-1)</td><td>91.601</td><td>17.858</td><td>2.126</td><td>-</td><td>-</td><td>-</td><td>-</td></tr>
<tr><td>lossyflac (-q X -C|-4)</td><td>90.036</td><td>18.028</td><td>2.169</td><td>-</td><td>-</td><td>-</td><td>-</td></tr>
<tr><td>lossyflac (-q X -C|-7)</td><td>87.338</td><td>19.909</td><td>2.184</td><td>-</td><td>-</td><td>-</td><td>-</td></tr>
<tr><td rowspan="4">lossytak(hybrid)</td><td>lossytak (-q I -C|-p2m)</td><td>84.998</td><td>22.941</td><td>2.264</td><td>-</td><td>-</td><td>-</td><td>-</td></tr>
<tr><td>lossytak (-q H -C|-p2m)</td><td>85.206</td><td>23.194</td><td>2.273</td><td>-</td><td>-</td><td>-</td><td>-</td></tr>
<tr><td>lossytak (-q S -C|-p2m)</td><td>85.291</td><td>23.223</td><td>2.273</td><td>-</td><td>-</td><td>-</td><td>-</td></tr>
<tr><td>lossytak (-q X -C|-p2m)</td><td>86.071</td><td>23.453</td><td>2.264</td><td>-</td><td>-</td><td>-</td><td>-</td></tr>
<tr><td rowspan="12">lossywv(hybrid)</td><td>lossywv (-q I -C|-f)</td><td>88.398</td><td>18.659</td><td>2.814</td><td>-</td><td>-</td><td>-</td><td>-</td></tr>
<tr><td>lossywv (-q I -C|)</td><td>87.411</td><td>19.035</td><td>2.983</td><td>-</td><td>-</td><td>-</td><td>-</td></tr>
<tr><td>lossywv (-q I -C|-h)</td><td>86.900</td><td>19.961</td><td>3.331</td><td>-</td><td>-</td><td>-</td><td>-</td></tr>
<tr><td>lossywv (-q H -C|-f)</td><td>87.831</td><td>18.858</td><td>2.799</td><td>-</td><td>-</td><td>-</td><td>-</td></tr>
<tr><td>lossywv (-q H -C|)</td><td>86.847</td><td>19.344</td><td>2.975</td><td>-</td><td>-</td><td>-</td><td>-</td></tr>
<tr><td>lossywv (-q H -C|-h)</td><td>86.444</td><td>20.108</td><td>3.309</td><td>-</td><td>-</td><td>-</td><td>-</td></tr>
<tr><td>lossywv (-q S -C|-f)</td><td>87.715</td><td>18.944</td><td>2.799</td><td>-</td><td>-</td><td>-</td><td>-</td></tr>
<tr><td>lossywv (-q S -C|)</td><td>86.748</td><td>19.304</td><td>3.105</td><td>-</td><td>-</td><td>-</td><td>-</td></tr>
<tr><td>lossywv (-q S -C|-h)</td><td>86.375</td><td>20.230</td><td>3.307</td><td>-</td><td>-</td><td>-</td><td>-</td></tr>
<tr><td>lossywv (-q X -C|-f)</td><td>87.508</td><td>19.057</td><td>2.825</td><td>-</td><td>-</td><td>-</td><td>-</td></tr>
<tr><td>lossywv (-q X -C|)</td><td>86.718</td><td>19.480</td><td>3.009</td><td>-</td><td>-</td><td>-</td><td>-</td></tr>
<tr><td>lossywv (-q X -C|-h)</td><td>86.474</td><td>20.251</td><td>3.408</td><td>-</td><td>-</td><td>-</td><td>-</td></tr>
<tr><td rowspan="2">alac</td><td>refalac (default)</td><td>79.243</td><td>1.539</td><td>0.773</td><td>-</td><td>-</td><td>-</td><td>-</td></tr>
<tr><td>refalac (--fast)</td><td>81.298</td><td>0.921</td><td>0.864</td><td>-</td><td>-</td><td>-</td><td>-</td></tr>
<tr><td colspan="9" style="text-align:center"> Lossy Codecs </td></tr><tr><td rowspan="10">mp3(CBR)</td><td>lame (-b128 -q2)</td><td>8.961</td><td>6.463</td><td>0.606</td><td>6.487</td><td>1.198</td><td>8.815</td><td>11.050</td></tr>
<tr><td>lame (-b128 -q7)</td><td>8.961</td><td>1.838</td><td>0.596</td><td>6.091</td><td>1.394</td><td>9.028</td><td>11.185</td></tr>
<tr><td>lame (-b160 -q2)</td><td>11.201</td><td>6.648</td><td>0.642</td><td>5.357</td><td>0.874</td><td>9.238</td><td>12.747</td></tr>
<tr><td>lame (-b160 -q7)</td><td>11.201</td><td>1.865</td><td>0.633</td><td>5.046</td><td>1.047</td><td>9.404</td><td>12.701</td></tr>
<tr><td>lame (-b192 -q2)</td><td>13.442</td><td>6.391</td><td>0.673</td><td>4.095</td><td>0.652</td><td>11.115</td><td>14.201</td></tr>
<tr><td>lame (-b192 -q7)</td><td>13.442</td><td>1.895</td><td>0.676</td><td>3.787</td><td>0.840</td><td>11.243</td><td>13.786</td></tr>
<tr><td>lame (-b256 -q2)</td><td>17.922</td><td>6.007</td><td>0.748</td><td>3.166</td><td>0.404</td><td>16.115</td><td>16.632</td></tr>
<tr><td>lame (-b256 -q7)</td><td>17.922</td><td>1.935</td><td>0.717</td><td>2.934</td><td>0.571</td><td>16.276</td><td>15.710</td></tr>
<tr><td>lame (-b320 -q2)</td><td>22.403</td><td>6.185</td><td>0.776</td><td>2.301</td><td>0.276</td><td>17.911</td><td>18.335</td></tr>
<tr><td>lame (-b320 -q7)</td><td>22.403</td><td>1.971</td><td>0.770</td><td>2.135</td><td>0.384</td><td>18.092</td><td>17.550</td></tr>
<tr><td rowspan="14">mp3(VBR)</td><td>lame (-V0 -q2)</td><td>17.566</td><td>3.418</td><td>0.752</td><td>2.172</td><td>0.428</td><td>15.841</td><td>16.283</td></tr>
<tr><td>lame (-V0 -q7)</td><td>17.333</td><td>1.980</td><td>0.731</td><td>1.804</td><td>0.596</td><td>15.361</td><td>14.969</td></tr>
<tr><td>lame (-V1 -q2)</td><td>15.030</td><td>3.270</td><td>0.700</td><td>3.722</td><td>0.543</td><td>14.632</td><td>15.249</td></tr>
<tr><td>lame (-V1 -q7)</td><td>14.965</td><td>1.922</td><td>0.683</td><td>3.440</td><td>0.723</td><td>14.369</td><td>14.060</td></tr>
<tr><td>lame (-V2 -q2)</td><td>12.725</td><td>3.201</td><td>0.680</td><td>4.530</td><td>0.710</td><td>13.367</td><td>13.961</td></tr>
<tr><td>lame (-V2 -q7)</td><td>13.133</td><td>1.906</td><td>0.667</td><td>4.117</td><td>0.886</td><td>13.380</td><td>13.074</td></tr>
<tr><td>lame (-V3 -q2)</td><td>11.427</td><td>3.116</td><td>0.642</td><td>5.299</td><td>0.843</td><td>12.466</td><td>12.970</td></tr>
<tr><td>lame (-V3 -q7)</td><td>11.803</td><td>1.911</td><td>0.660</td><td>5.114</td><td>1.087</td><td>11.826</td><td>11.733</td></tr>
<tr><td>lame (-V4 -q2)</td><td>10.031</td><td>3.045</td><td>0.622</td><td>6.032</td><td>1.024</td><td>11.515</td><td>12.071</td></tr>
<tr><td>lame (-V4 -q7)</td><td>10.877</td><td>1.918</td><td>0.641</td><td>5.677</td><td>1.235</td><td>11.198</td><td>11.066</td></tr>
<tr><td>lame (-V5 -q2)</td><td>8.671</td><td>2.973</td><td>0.592</td><td>6.790</td><td>1.305</td><td>10.485</td><td>10.743</td></tr>
<tr><td>lame (-V5 -q7)</td><td>10.013</td><td>1.897</td><td>0.599</td><td>6.185</td><td>1.456</td><td>10.406</td><td>10.233</td></tr>
<tr><td>lame (-V6 -q2)</td><td>7.760</td><td>2.928</td><td>0.578</td><td>7.285</td><td>1.604</td><td>9.518</td><td>9.719</td></tr>
<tr><td>lame (-V6 -q7)</td><td>9.476</td><td>1.886</td><td>0.594</td><td>6.320</td><td>1.694</td><td>9.703</td><td>9.410</td></tr>
<tr><td rowspan="5">wavpack</td><td>wavpack (-b128)</td><td>15.282</td><td>1.385</td><td>0.871</td><td>2.928</td><td>1.146</td><td>13.657</td><td>13.160</td></tr>
<tr><td>wavpack (-b160)</td><td>15.282</td><td>1.364</td><td>0.863</td><td>2.928</td><td>1.146</td><td>13.657</td><td>13.160</td></tr>
<tr><td>wavpack (-b192)</td><td>15.282</td><td>1.365</td><td>0.865</td><td>2.928</td><td>1.146</td><td>13.657</td><td>13.160</td></tr>
<tr><td>wavpack (-b256)</td><td>19.681</td><td>1.559</td><td>0.972</td><td>1.368</td><td>0.478</td><td>18.132</td><td>17.428</td></tr>
<tr><td>wavpack (-b320)</td><td>24.607</td><td>1.680</td><td>1.095</td><td>0.759</td><td>0.258</td><td>20.973</td><td>20.261</td></tr>
<tr><td rowspan="12">wma(CBR)</td><td>wmaencode (-c pro -m cbr -b 128)</td><td>9.028</td><td>2.649</td><td>0.316</td><td>6.173</td><td>1.600</td><td>11.435</td><td>9.996</td></tr>
<tr><td>wmaencode (-c pro -m cbr -b 160)</td><td>11.270</td><td>2.643</td><td>0.303</td><td>4.131</td><td>1.364</td><td>12.510</td><td>10.891</td></tr>
<tr><td>wmaencode (-c pro -m cbr -b 192)</td><td>13.512</td><td>2.797</td><td>0.328</td><td>3.629</td><td>1.154</td><td>13.451</td><td>12.067</td></tr>
<tr><td>wmaencode (-c pro -m cbr -b 256)</td><td>17.995</td><td>2.955</td><td>0.351</td><td>1.422</td><td>0.755</td><td>15.669</td><td>14.123</td></tr>
<tr><td>wmaencode (-c pro -m cbr -b 384)</td><td>26.963</td><td>4.067</td><td>0.400</td><td>0.621</td><td>0.326</td><td>19.636</td><td>18.172</td></tr>
<tr><td>wmaencode (-c pro -m cbr -b 440)</td><td>30.887</td><td>3.926</td><td>0.438</td><td>0.451</td><td>0.234</td><td>21.143</td><td>19.492</td></tr>
<tr><td>wmaencode (-c pro -m cbr2pass -b 128)</td><td>9.028</td><td>9.388</td><td>0.301</td><td>6.167</td><td>1.588</td><td>11.495</td><td>10.260</td></tr>
<tr><td>wmaencode (-c pro -m cbr2pass -b 160)</td><td>11.270</td><td>10.373</td><td>0.305</td><td>4.130</td><td>1.356</td><td>12.587</td><td>11.091</td></tr>
<tr><td>wmaencode (-c pro -m cbr2pass -b 192)</td><td>13.512</td><td>10.892</td><td>0.329</td><td>3.619</td><td>1.145</td><td>13.546</td><td>12.170</td></tr>
<tr><td>wmaencode (-c pro -m cbr2pass -b 256)</td><td>17.995</td><td>12.289</td><td>0.375</td><td>1.400</td><td>0.746</td><td>15.781</td><td>14.227</td></tr>
<tr><td>wmaencode (-c pro -m cbr2pass -b 384)</td><td>26.963</td><td>14.330</td><td>1.687</td><td>0.612</td><td>0.321</td><td>19.724</td><td>18.190</td></tr>
<tr><td>wmaencode (-c pro -m cbr2pass -b 440)</td><td>30.887</td><td>13.855</td><td>0.432</td><td>0.441</td><td>0.230</td><td>21.277</td><td>19.772</td></tr>
<tr><td rowspan="12">wma(VBR)</td><td>wmaencode (-c pro -m vbr -q 10)</td><td>3.905</td><td>6.621</td><td>0.237</td><td>11.012</td><td>3.397</td><td>6.891</td><td>5.774</td></tr>
<tr><td>wmaencode (-c pro -m vbr -q 25)</td><td>5.519</td><td>3.748</td><td>0.274</td><td>6.869</td><td>2.360</td><td>9.045</td><td>7.778</td></tr>
<tr><td>wmaencode (-c pro -m vbr -q 50)</td><td>7.927</td><td>3.844</td><td>0.278</td><td>6.441</td><td>1.909</td><td>10.591</td><td>9.137</td></tr>
<tr><td>wmaencode (-c pro -m vbr -q 75)</td><td>9.651</td><td>3.880</td><td>0.307</td><td>4.443</td><td>1.757</td><td>11.232</td><td>9.805</td></tr>
<tr><td>wmaencode (-c pro -m vbr -q 90)</td><td>11.737</td><td>3.996</td><td>0.302</td><td>2.739</td><td>1.440</td><td>12.383</td><td>10.876</td></tr>
<tr><td>wmaencode (-c pro -m vbr -q 98)</td><td>18.610</td><td>4.144</td><td>0.352</td><td>1.293</td><td>0.688</td><td>16.114</td><td>14.561</td></tr>
<tr><td>wmaencode (-c pro -m vbr2pass -q 10)</td><td>9.059</td><td>8.214</td><td>0.280</td><td>6.156</td><td>1.639</td><td>11.401</td><td>9.927</td></tr>
<tr><td>wmaencode (-c pro -m vbr2pass -q 25)</td><td>9.059</td><td>8.214</td><td>0.286</td><td>6.156</td><td>1.639</td><td>11.401</td><td>9.927</td></tr>
<tr><td>wmaencode (-c pro -m vbr2pass -q 50)</td><td>9.059</td><td>8.168</td><td>0.285</td><td>6.156</td><td>1.639</td><td>11.401</td><td>9.927</td></tr>
<tr><td>wmaencode (-c pro -m vbr2pass -q 75)</td><td>9.059</td><td>8.236</td><td>0.282</td><td>6.156</td><td>1.639</td><td>11.401</td><td>9.927</td></tr>
<tr><td>wmaencode (-c pro -m vbr2pass -q 90)</td><td>9.059</td><td>8.262</td><td>0.287</td><td>6.156</td><td>1.639</td><td>11.401</td><td>9.927</td></tr>
<tr><td>wmaencode (-c pro -m vbr2pass -q 98)</td><td>9.059</td><td>8.244</td><td>0.287</td><td>6.156</td><td>1.639</td><td>11.401</td><td>9.927</td></tr>
<tr><td rowspan="5">opus</td><td>opus (--bitrate 64)</td><td>4.302</td><td>4.093</td><td>1.784</td><td>5.263</td><td>2.490</td><td>8.507</td><td>7.673</td></tr>
<tr><td>opus (--bitrate 80)</td><td>5.377</td><td>3.706</td><td>1.801</td><td>4.933</td><td>2.068</td><td>9.427</td><td>8.250</td></tr>
<tr><td>opus (--bitrate 96)</td><td>6.469</td><td>3.883</td><td>1.874</td><td>4.611</td><td>1.820</td><td>10.042</td><td>8.661</td></tr>
<tr><td>opus (--bitrate 128)</td><td>8.660</td><td>4.221</td><td>1.953</td><td>3.972</td><td>1.454</td><td>11.214</td><td>10.008</td></tr>
<tr><td>opus (--bitrate 160)</td><td>10.789</td><td>4.484</td><td>2.033</td><td>3.275</td><td>1.238</td><td>12.206</td><td>11.092</td></tr>
<tr><td rowspan="12">lossyflac</td><td>lossyflac (-q I|-1)</td><td>47.179</td><td>17.456</td><td>0.355</td><td>0.125</td><td>0.064</td><td>26.654</td><td>24.876</td></tr>
<tr><td>lossyflac (-q I|-4)</td><td>45.527</td><td>17.064</td><td>0.403</td><td>0.125</td><td>0.064</td><td>26.654</td><td>24.876</td></tr>
<tr><td>lossyflac (-q I|-7)</td><td>42.173</td><td>17.902</td><td>0.395</td><td>0.125</td><td>0.064</td><td>26.654</td><td>24.876</td></tr>
<tr><td>lossyflac (-q H|-1)</td><td>38.985</td><td>17.141</td><td>0.354</td><td>0.301</td><td>0.157</td><td>22.959</td><td>21.154</td></tr>
<tr><td>lossyflac (-q H|-4)</td><td>37.388</td><td>17.304</td><td>0.385</td><td>0.301</td><td>0.157</td><td>22.959</td><td>21.154</td></tr>
<tr><td>lossyflac (-q H|-7)</td><td>34.359</td><td>18.258</td><td>0.384</td><td>0.301</td><td>0.157</td><td>22.959</td><td>21.154</td></tr>
<tr><td>lossyflac (-q S|-1)</td><td>37.226</td><td>17.293</td><td>0.358</td><td>0.361</td><td>0.186</td><td>22.216</td><td>20.945</td></tr>
<tr><td>lossyflac (-q S|-4)</td><td>35.668</td><td>17.398</td><td>0.406</td><td>0.361</td><td>0.186</td><td>22.216</td><td>20.945</td></tr>
<tr><td>lossyflac (-q S|-7)</td><td>32.739</td><td>18.459</td><td>0.381</td><td>0.361</td><td>0.186</td><td>22.216</td><td>20.945</td></tr>
<tr><td>lossyflac (-q X|-1)</td><td>29.803</td><td>17.452</td><td>0.349</td><td>0.781</td><td>0.404</td><td>19.093</td><td>17.880</td></tr>
<tr><td>lossyflac (-q X|-4)</td><td>28.732</td><td>17.612</td><td>0.388</td><td>0.781</td><td>0.404</td><td>19.093</td><td>17.880</td></tr>
<tr><td>lossyflac (-q X|-7)</td><td>26.233</td><td>18.558</td><td>0.370</td><td>0.781</td><td>0.404</td><td>19.093</td><td>17.880</td></tr>
<tr><td rowspan="4">lossytak</td><td>lossytak (-q I|-p2m)</td><td>41.322</td><td>20.376</td><td>0.463</td><td>0.125</td><td>0.064</td><td>26.654</td><td>24.876</td></tr>
<tr><td>lossytak (-q H|-p2m)</td><td>33.463</td><td>19.994</td><td>0.453</td><td>0.301</td><td>0.157</td><td>22.959</td><td>21.154</td></tr>
<tr><td>lossytak (-q S|-p2m)</td><td>31.813</td><td>20.074</td><td>0.446</td><td>0.361</td><td>0.186</td><td>22.216</td><td>20.945</td></tr>
<tr><td>lossytak (-q X|-p2m)</td><td>25.122</td><td>20.174</td><td>0.428</td><td>0.781</td><td>0.404</td><td>19.093</td><td>17.880</td></tr>
<tr><td rowspan="12">lossywv</td><td>lossywv (-q I|-f)</td><td>44.911</td><td>17.787</td><td>0.776</td><td>0.125</td><td>0.064</td><td>26.654</td><td>24.876</td></tr>
<tr><td>lossywv (-q I|)</td><td>44.194</td><td>18.191</td><td>0.843</td><td>0.125</td><td>0.064</td><td>26.654</td><td>24.876</td></tr>
<tr><td>lossywv (-q I|-h)</td><td>44.098</td><td>18.722</td><td>1.011</td><td>0.125</td><td>0.064</td><td>26.654</td><td>24.876</td></tr>
<tr><td>lossywv (-q H|-f)</td><td>36.408</td><td>18.045</td><td>0.736</td><td>0.301</td><td>0.157</td><td>22.959</td><td>21.154</td></tr>
<tr><td>lossywv (-q H|)</td><td>35.728</td><td>18.296</td><td>0.818</td><td>0.301</td><td>0.157</td><td>22.959</td><td>21.154</td></tr>
<tr><td>lossywv (-q H|-h)</td><td>35.654</td><td>18.957</td><td>0.989</td><td>0.301</td><td>0.157</td><td>22.959</td><td>21.154</td></tr>
<tr><td>lossywv (-q S|-f)</td><td>34.598</td><td>18.038</td><td>0.730</td><td>0.361</td><td>0.186</td><td>22.216</td><td>20.945</td></tr>
<tr><td>lossywv (-q S|)</td><td>33.945</td><td>18.540</td><td>0.869</td><td>0.361</td><td>0.186</td><td>22.216</td><td>20.945</td></tr>
<tr><td>lossywv (-q S|-h)</td><td>33.880</td><td>19.142</td><td>0.981</td><td>0.361</td><td>0.186</td><td>22.216</td><td>20.945</td></tr>
<tr><td>lossywv (-q X|-f)</td><td>27.059</td><td>18.266</td><td>0.708</td><td>0.781</td><td>0.404</td><td>19.093</td><td>17.880</td></tr>
<tr><td>lossywv (-q X|)</td><td>26.642</td><td>18.592</td><td>0.798</td><td>0.781</td><td>0.404</td><td>19.093</td><td>17.880</td></tr>
<tr><td>lossywv (-q X|-h)</td><td>26.631</td><td>19.115</td><td>0.985</td><td>0.781</td><td>0.404</td><td>19.093</td><td>17.880</td></tr>
<tr><td rowspan="8">aac(VBR)</td><td>neroaac (-q 0.1)</td><td>1.796</td><td>2.877</td><td>1.539</td><td>9.055</td><td>3.000</td><td>7.541</td><td>6.636</td></tr>
<tr><td>neroaac (-q 0.3)</td><td>5.828</td><td>4.119</td><td>0.993</td><td>7.805</td><td>1.085</td><td>10.882</td><td>12.217</td></tr>
<tr><td>neroaac (-q 0.5)</td><td>12.825</td><td>4.400</td><td>0.545</td><td>3.866</td><td>0.830</td><td>14.109</td><td>13.559</td></tr>
<tr><td>neroaac (-q 0.7)</td><td>19.544</td><td>4.672</td><td>0.623</td><td>1.518</td><td>0.585</td><td>15.606</td><td>14.945</td></tr>
<tr><td>neroaac (-q 0.9)</td><td>25.471</td><td>4.690</td><td>0.692</td><td>0.690</td><td>0.442</td><td>16.931</td><td>16.016</td></tr>
<tr><td>qaac (-V 31)</td><td>4.502</td><td>4.484</td><td>0.560</td><td>9.808</td><td>2.498</td><td>8.353</td><td>7.600</td></tr>
<tr><td>qaac (-V 63)</td><td>8.540</td><td>3.843</td><td>0.619</td><td>5.795</td><td>1.125</td><td>11.863</td><td>11.729</td></tr>
<tr><td>qaac (-V 95)</td><td>13.492</td><td>3.866</td><td>0.669</td><td>3.388</td><td>0.630</td><td>14.698</td><td>14.393</td></tr>
<tr><td rowspan="10">aac(CBR)</td><td>neroaac (-cbr 128)</td><td>0.895</td><td>2.055</td><td>1.067</td><td>14.594</td><td>5.214</td><td>5.260</td><td>4.277</td></tr>
<tr><td>neroaac (-cbr 160)</td><td>0.895</td><td>2.053</td><td>1.067</td><td>14.594</td><td>5.214</td><td>5.260</td><td>4.277</td></tr>
<tr><td>neroaac (-cbr 192)</td><td>0.895</td><td>2.065</td><td>1.059</td><td>14.594</td><td>5.214</td><td>5.260</td><td>4.277</td></tr>
<tr><td>neroaac (-cbr 256)</td><td>0.895</td><td>2.110</td><td>1.080</td><td>14.594</td><td>5.214</td><td>5.260</td><td>4.277</td></tr>
<tr><td>neroaac (-cbr 320)</td><td>0.895</td><td>2.107</td><td>1.061</td><td>14.594</td><td>5.214</td><td>5.260</td><td>4.277</td></tr>
<tr><td>qaac (-c 128)</td><td>9.068</td><td>3.934</td><td>0.621</td><td>5.666</td><td>1.090</td><td>12.014</td><td>11.855</td></tr>
<tr><td>qaac (-c 160)</td><td>11.308</td><td>4.069</td><td>0.653</td><td>4.536</td><td>0.878</td><td>13.065</td><td>12.874</td></tr>
<tr><td>qaac (-c 192)</td><td>13.549</td><td>4.081</td><td>0.680</td><td>3.472</td><td>0.674</td><td>14.334</td><td>13.999</td></tr>
<tr><td>qaac (-c 256)</td><td>18.029</td><td>4.366</td><td>0.718</td><td>1.347</td><td>0.448</td><td>16.104</td><td>15.471</td></tr>
<tr><td>qaac (-c 320)</td><td>22.510</td><td>4.401</td><td>0.741</td><td>0.859</td><td>0.284</td><td>18.136</td><td>17.486</td></tr>
<tr><td rowspan="3">vorbis</td><td>oggenc (-q 2)</td><td>6.295</td><td>7.454</td><td>0.351</td><td>6.570</td><td>1.784</td><td>10.309</td><td>9.893</td></tr>
<tr><td>oggenc (-q 7)</td><td>14.771</td><td>5.352</td><td>0.401</td><td>2.366</td><td>0.711</td><td>14.961</td><td>14.876</td></tr>
<tr><td>oggenc (-q 10)</td><td>32.028</td><td>5.831</td><td>0.521</td><td>0.433</td><td>0.245</td><td>18.243</td><td>19.987</td></tr>
<tr><td rowspan="3">musepack</td><td>mpc (--standard)</td><td>12.134</td><td>4.620</td><td>1.172</td><td>3.965</td><td>0.693</td><td>14.366</td><td>13.941</td></tr>
<tr><td>mpc (--extreme)</td><td>14.294</td><td>4.353</td><td>0.635</td><td>2.953</td><td>0.521</td><td>15.463</td><td>15.219</td></tr>
<tr><td>mpc (--insane)</td><td>16.325</td><td>4.391</td><td>0.680</td><td>2.087</td><td>0.403</td><td>16.573</td><td>16.492</td></tr>
</table>

# Results for `久石让 - あの夏へ.wav`
Audio Format: 2ch, 16-bit, 44100 Hz, 8370180 samples
<table><tr><th rowspan="2">Format</th><th rowspan="2">Codec</th><th rowspan="2">Compression Ratio (%)</th><th rowspan="2">Encoding time (s)</th><th rowspan="2">Decoding time (s)</th><th colspan="2">Spectrogram Error (db)</th><th colspan="2">Signal-to-Noise Ratio (db)</th></tr>
<tr><th>linear</th><th>weighted</th><th>linear</th><th>weighted</th></tr>
<tr><td colspan="9" style="text-align:center"> Lossless Codecs </td></tr>
<tr><td rowspan="3">optimFrog</td><td>ofr (--preset 0)</td><td>44.761</td><td>1.184</td><td>1.717</td><td>-</td><td>-</td><td>-</td><td>-</td></tr>
<tr><td>ofr (--preset 5)</td><td>43.409</td><td>5.129</td><td>4.221</td><td>-</td><td>-</td><td>-</td><td>-</td></tr>
<tr><td>ofr (--preset 10)</td><td>42.407</td><td>23.404</td><td>11.808</td><td>-</td><td>-</td><td>-</td><td>-</td></tr>
<tr><td rowspan="8">flac</td><td>flac (-0)</td><td>52.850</td><td>0.223</td><td>0.173</td><td>-</td><td>-</td><td>-</td><td>-</td></tr>
<tr><td>flac (-1)</td><td>52.825</td><td>0.222</td><td>0.174</td><td>-</td><td>-</td><td>-</td><td>-</td></tr>
<tr><td>flac (-2)</td><td>52.760</td><td>0.252</td><td>0.169</td><td>-</td><td>-</td><td>-</td><td>-</td></tr>
<tr><td>flac (-3)</td><td>46.275</td><td>0.219</td><td>0.181</td><td>-</td><td>-</td><td>-</td><td>-</td></tr>
<tr><td>flac (-4)</td><td>45.876</td><td>0.261</td><td>0.191</td><td>-</td><td>-</td><td>-</td><td>-</td></tr>
<tr><td>flac (-5)</td><td>45.829</td><td>0.283</td><td>0.196</td><td>-</td><td>-</td><td>-</td><td>-</td></tr>
<tr><td>flac (-6)</td><td>45.794</td><td>0.383</td><td>0.189</td><td>-</td><td>-</td><td>-</td><td>-</td></tr>
<tr><td>flac (-7)</td><td>45.712</td><td>0.502</td><td>0.208</td><td>-</td><td>-</td><td>-</td><td>-</td></tr>
<tr><td rowspan="5">ape</td><td>mac (-c1000)</td><td>46.523</td><td>1.113</td><td>1.310</td><td>-</td><td>-</td><td>-</td><td>-</td></tr>
<tr><td>mac (-c2000)</td><td>44.916</td><td>1.568</td><td>1.745</td><td>-</td><td>-</td><td>-</td><td>-</td></tr>
<tr><td>mac (-c3000)</td><td>44.467</td><td>1.642</td><td>1.818</td><td>-</td><td>-</td><td>-</td><td>-</td></tr>
<tr><td>mac (-c4000)</td><td>43.645</td><td>2.391</td><td>2.429</td><td>-</td><td>-</td><td>-</td><td>-</td></tr>
<tr><td>mac (-c5000)</td><td>43.208</td><td>4.681</td><td>4.422</td><td>-</td><td>-</td><td>-</td><td>-</td></tr>
<tr><td rowspan="6">wavpack</td><td>wavpack (-f)</td><td>52.526</td><td>0.444</td><td>0.388</td><td>-</td><td>-</td><td>-</td><td>-</td></tr>
<tr><td>wavpack (default)</td><td>47.231</td><td>0.483</td><td>0.420</td><td>-</td><td>-</td><td>-</td><td>-</td></tr>
<tr><td>wavpack (-h)</td><td>46.621</td><td>0.630</td><td>0.520</td><td>-</td><td>-</td><td>-</td><td>-</td></tr>
<tr><td>wavpack (-hh)</td><td>45.754</td><td>0.773</td><td>0.650</td><td>-</td><td>-</td><td>-</td><td>-</td></tr>
<tr><td>wavpack (-h -x1)</td><td>45.952</td><td>1.041</td><td>0.503</td><td>-</td><td>-</td><td>-</td><td>-</td></tr>
<tr><td>wavpack (-hh -x3)</td><td>45.464</td><td>4.678</td><td>0.612</td><td>-</td><td>-</td><td>-</td><td>-</td></tr>
<tr><td rowspan="4">wavpack(hybrid)</td><td>wavpack (-c -b192 -f)</td><td>54.446</td><td>0.745</td><td>0.553</td><td>-</td><td>-</td><td>-</td><td>-</td></tr>
<tr><td>wavpack (-c -b192)</td><td>49.505</td><td>0.834</td><td>0.634</td><td>-</td><td>-</td><td>-</td><td>-</td></tr>
<tr><td>wavpack (-c -b192 -h)</td><td>48.972</td><td>1.015</td><td>0.801</td><td>-</td><td>-</td><td>-</td><td>-</td></tr>
<tr><td>wavpack (-c -b192 -hh)</td><td>48.562</td><td>1.201</td><td>0.961</td><td>-</td><td>-</td><td>-</td><td>-</td></tr>
<tr><td rowspan="30">tak</td><td>takc (-p0 -tn1)</td><td>46.511</td><td>0.197</td><td>0.209</td><td>-</td><td>-</td><td>-</td><td>-</td></tr>
<tr><td>takc (-p0 -tn4)</td><td>46.511</td><td>0.085</td><td>0.204</td><td>-</td><td>-</td><td>-</td><td>-</td></tr>
<tr><td>takc (-p0e -tn1)</td><td>46.415</td><td>0.213</td><td>0.202</td><td>-</td><td>-</td><td>-</td><td>-</td></tr>
<tr><td>takc (-p0e -tn4)</td><td>46.415</td><td>0.081</td><td>0.203</td><td>-</td><td>-</td><td>-</td><td>-</td></tr>
<tr><td>takc (-p0m -tn1)</td><td>46.331</td><td>0.356</td><td>0.204</td><td>-</td><td>-</td><td>-</td><td>-</td></tr>
<tr><td>takc (-p0m -tn4)</td><td>46.331</td><td>0.104</td><td>0.203</td><td>-</td><td>-</td><td>-</td><td>-</td></tr>
<tr><td>takc (-p1 -tn1)</td><td>45.166</td><td>0.196</td><td>0.204</td><td>-</td><td>-</td><td>-</td><td>-</td></tr>
<tr><td>takc (-p1 -tn4)</td><td>45.166</td><td>0.079</td><td>0.208</td><td>-</td><td>-</td><td>-</td><td>-</td></tr>
<tr><td>takc (-p1e -tn1)</td><td>45.116</td><td>0.314</td><td>0.208</td><td>-</td><td>-</td><td>-</td><td>-</td></tr>
<tr><td>takc (-p1e -tn4)</td><td>45.116</td><td>0.098</td><td>0.207</td><td>-</td><td>-</td><td>-</td><td>-</td></tr>
<tr><td>takc (-p1m -tn1)</td><td>45.051</td><td>0.491</td><td>0.204</td><td>-</td><td>-</td><td>-</td><td>-</td></tr>
<tr><td>takc (-p1m -tn4)</td><td>45.051</td><td>0.140</td><td>0.214</td><td>-</td><td>-</td><td>-</td><td>-</td></tr>
<tr><td>takc (-p2 -tn1)</td><td>44.805</td><td>0.258</td><td>0.242</td><td>-</td><td>-</td><td>-</td><td>-</td></tr>
<tr><td>takc (-p2 -tn4)</td><td>44.805</td><td>0.081</td><td>0.243</td><td>-</td><td>-</td><td>-</td><td>-</td></tr>
<tr><td>takc (-p2e -tn1)</td><td>44.766</td><td>0.455</td><td>0.240</td><td>-</td><td>-</td><td>-</td><td>-</td></tr>
<tr><td>takc (-p2e -tn4)</td><td>44.766</td><td>0.140</td><td>0.240</td><td>-</td><td>-</td><td>-</td><td>-</td></tr>
<tr><td>takc (-p2m -tn1)</td><td>44.694</td><td>0.828</td><td>0.242</td><td>-</td><td>-</td><td>-</td><td>-</td></tr>
<tr><td>takc (-p2m -tn4)</td><td>44.694</td><td>0.224</td><td>0.241</td><td>-</td><td>-</td><td>-</td><td>-</td></tr>
<tr><td>takc (-p3 -tn1)</td><td>44.222</td><td>0.508</td><td>0.245</td><td>-</td><td>-</td><td>-</td><td>-</td></tr>
<tr><td>takc (-p3 -tn4)</td><td>44.222</td><td>0.143</td><td>0.253</td><td>-</td><td>-</td><td>-</td><td>-</td></tr>
<tr><td>takc (-p3e -tn1)</td><td>44.179</td><td>0.633</td><td>0.247</td><td>-</td><td>-</td><td>-</td><td>-</td></tr>
<tr><td>takc (-p3e -tn4)</td><td>44.179</td><td>0.181</td><td>0.252</td><td>-</td><td>-</td><td>-</td><td>-</td></tr>
<tr><td>takc (-p3m -tn1)</td><td>44.158</td><td>1.209</td><td>0.247</td><td>-</td><td>-</td><td>-</td><td>-</td></tr>
<tr><td>takc (-p3m -tn4)</td><td>44.158</td><td>0.328</td><td>0.251</td><td>-</td><td>-</td><td>-</td><td>-</td></tr>
<tr><td>takc (-p4 -tn1)</td><td>43.855</td><td>0.810</td><td>0.280</td><td>-</td><td>-</td><td>-</td><td>-</td></tr>
<tr><td>takc (-p4 -tn4)</td><td>43.855</td><td>0.228</td><td>0.284</td><td>-</td><td>-</td><td>-</td><td>-</td></tr>
<tr><td>takc (-p4e -tn1)</td><td>43.842</td><td>0.967</td><td>0.278</td><td>-</td><td>-</td><td>-</td><td>-</td></tr>
<tr><td>takc (-p4e -tn4)</td><td>43.842</td><td>0.263</td><td>0.278</td><td>-</td><td>-</td><td>-</td><td>-</td></tr>
<tr><td>takc (-p4m -tn1)</td><td>43.823</td><td>1.812</td><td>0.281</td><td>-</td><td>-</td><td>-</td><td>-</td></tr>
<tr><td>takc (-p4m -tn4)</td><td>43.823</td><td>0.499</td><td>0.281</td><td>-</td><td>-</td><td>-</td><td>-</td></tr>
<tr><td rowspan="1">tta</td><td>tta (default)</td><td>46.625</td><td>0.380</td><td>0.421</td><td>-</td><td>-</td><td>-</td><td>-</td></tr>
<tr><td rowspan="1">wma</td><td>wmaencode (-c lsl)</td><td>48.987</td><td>1.338</td><td>0.574</td><td>-</td><td>-</td><td>-</td><td>-</td></tr>
<tr><td rowspan="12">lossyflac(hybrid)</td><td>lossyflac (-q I -C|-1)</td><td>55.305</td><td>4.250</td><td>1.129</td><td>-</td><td>-</td><td>-</td><td>-</td></tr>
<tr><td>lossyflac (-q I -C|-4)</td><td>49.825</td><td>4.308</td><td>1.164</td><td>-</td><td>-</td><td>-</td><td>-</td></tr>
<tr><td>lossyflac (-q I -C|-7)</td><td>49.500</td><td>4.973</td><td>1.172</td><td>-</td><td>-</td><td>-</td><td>-</td></tr>
<tr><td>lossyflac (-q H -C|-1)</td><td>58.561</td><td>7.766</td><td>1.168</td><td>-</td><td>-</td><td>-</td><td>-</td></tr>
<tr><td>lossyflac (-q H -C|-4)</td><td>52.949</td><td>7.855</td><td>1.197</td><td>-</td><td>-</td><td>-</td><td>-</td></tr>
<tr><td>lossyflac (-q H -C|-7)</td><td>52.548</td><td>8.731</td><td>1.195</td><td>-</td><td>-</td><td>-</td><td>-</td></tr>
<tr><td>lossyflac (-q S -C|-1)</td><td>59.316</td><td>8.391</td><td>1.205</td><td>-</td><td>-</td><td>-</td><td>-</td></tr>
<tr><td>lossyflac (-q S -C|-4)</td><td>53.475</td><td>8.488</td><td>1.198</td><td>-</td><td>-</td><td>-</td><td>-</td></tr>
<tr><td>lossyflac (-q S -C|-7)</td><td>52.983</td><td>9.390</td><td>1.195</td><td>-</td><td>-</td><td>-</td><td>-</td></tr>
<tr><td>lossyflac (-q X -C|-1)</td><td>62.541</td><td>10.312</td><td>1.188</td><td>-</td><td>-</td><td>-</td><td>-</td></tr>
<tr><td>lossyflac (-q X -C|-4)</td><td>55.441</td><td>10.474</td><td>1.228</td><td>-</td><td>-</td><td>-</td><td>-</td></tr>
<tr><td>lossyflac (-q X -C|-7)</td><td>54.876</td><td>11.526</td><td>1.225</td><td>-</td><td>-</td><td>-</td><td>-</td></tr>
<tr><td rowspan="4">lossytak(hybrid)</td><td>lossytak (-q I -C|-p2m)</td><td>48.306</td><td>6.262</td><td>1.197</td><td>-</td><td>-</td><td>-</td><td>-</td></tr>
<tr><td>lossytak (-q H -C|-p2m)</td><td>49.989</td><td>10.367</td><td>1.251</td><td>-</td><td>-</td><td>-</td><td>-</td></tr>
<tr><td>lossytak (-q S -C|-p2m)</td><td>50.141</td><td>11.059</td><td>1.346</td><td>-</td><td>-</td><td>-</td><td>-</td></tr>
<tr><td>lossytak (-q X -C|-p2m)</td><td>51.469</td><td>13.289</td><td>1.263</td><td>-</td><td>-</td><td>-</td><td>-</td></tr>
<tr><td rowspan="12">lossywv(hybrid)</td><td>lossywv (-q I -C|-f)</td><td>55.301</td><td>4.564</td><td>1.350</td><td>-</td><td>-</td><td>-</td><td>-</td></tr>
<tr><td>lossywv (-q I -C|)</td><td>49.929</td><td>5.792</td><td>1.447</td><td>-</td><td>-</td><td>-</td><td>-</td></tr>
<tr><td>lossywv (-q I -C|-h)</td><td>49.322</td><td>4.993</td><td>1.618</td><td>-</td><td>-</td><td>-</td><td>-</td></tr>
<tr><td>lossywv (-q H -C|-f)</td><td>60.330</td><td>8.226</td><td>1.688</td><td>-</td><td>-</td><td>-</td><td>-</td></tr>
<tr><td>lossywv (-q H -C|)</td><td>54.363</td><td>8.443</td><td>1.561</td><td>-</td><td>-</td><td>-</td><td>-</td></tr>
<tr><td>lossywv (-q H -C|-h)</td><td>54.046</td><td>8.923</td><td>1.767</td><td>-</td><td>-</td><td>-</td><td>-</td></tr>
<tr><td>lossywv (-q S -C|-f)</td><td>60.849</td><td>8.897</td><td>1.489</td><td>-</td><td>-</td><td>-</td><td>-</td></tr>
<tr><td>lossywv (-q S -C|)</td><td>54.590</td><td>9.184</td><td>1.584</td><td>-</td><td>-</td><td>-</td><td>-</td></tr>
<tr><td>lossywv (-q S -C|-h)</td><td>54.290</td><td>9.646</td><td>1.790</td><td>-</td><td>-</td><td>-</td><td>-</td></tr>
<tr><td>lossywv (-q X -C|-f)</td><td>64.354</td><td>10.960</td><td>1.566</td><td>-</td><td>-</td><td>-</td><td>-</td></tr>
<tr><td>lossywv (-q X -C|)</td><td>56.702</td><td>11.308</td><td>1.672</td><td>-</td><td>-</td><td>-</td><td>-</td></tr>
<tr><td>lossywv (-q X -C|-h)</td><td>56.356</td><td>11.851</td><td>1.897</td><td>-</td><td>-</td><td>-</td><td>-</td></tr>
<tr><td rowspan="2">alac</td><td>refalac (default)</td><td>47.568</td><td>0.810</td><td>0.393</td><td>-</td><td>-</td><td>-</td><td>-</td></tr>
<tr><td>refalac (--fast)</td><td>48.031</td><td>0.514</td><td>0.478</td><td>-</td><td>-</td><td>-</td><td>-</td></tr>
<tr><td colspan="9" style="text-align:center"> Lossy Codecs </td></tr><tr><td rowspan="10">mp3(CBR)</td><td>lame (-b128 -q2)</td><td>9.073</td><td>3.182</td><td>0.306</td><td>0.756</td><td>0.824</td><td>9.649</td><td>12.562</td></tr>
<tr><td>lame (-b128 -q7)</td><td>9.073</td><td>0.968</td><td>0.288</td><td>0.636</td><td>0.366</td><td>9.978</td><td>15.619</td></tr>
<tr><td>lame (-b160 -q2)</td><td>11.341</td><td>3.615</td><td>0.328</td><td>0.597</td><td>0.605</td><td>9.857</td><td>13.972</td></tr>
<tr><td>lame (-b160 -q7)</td><td>11.341</td><td>0.974</td><td>0.301</td><td>0.481</td><td>0.249</td><td>10.027</td><td>17.192</td></tr>
<tr><td>lame (-b192 -q2)</td><td>13.609</td><td>2.392</td><td>0.336</td><td>0.440</td><td>0.335</td><td>12.057</td><td>17.771</td></tr>
<tr><td>lame (-b192 -q7)</td><td>13.609</td><td>1.024</td><td>0.328</td><td>0.388</td><td>0.186</td><td>12.180</td><td>19.574</td></tr>
<tr><td>lame (-b256 -q2)</td><td>18.146</td><td>2.461</td><td>0.371</td><td>0.302</td><td>0.203</td><td>20.686</td><td>20.322</td></tr>
<tr><td>lame (-b256 -q7)</td><td>18.146</td><td>1.020</td><td>0.356</td><td>0.276</td><td>0.124</td><td>22.746</td><td>20.313</td></tr>
<tr><td>lame (-b320 -q2)</td><td>22.682</td><td>2.675</td><td>0.402</td><td>0.221</td><td>0.131</td><td>22.989</td><td>22.035</td></tr>
<tr><td>lame (-b320 -q7)</td><td>22.682</td><td>1.036</td><td>0.388</td><td>0.207</td><td>0.082</td><td>24.605</td><td>24.419</td></tr>
<tr><td rowspan="14">mp3(VBR)</td><td>lame (-V0 -q2)</td><td>18.961</td><td>1.794</td><td>0.381</td><td>0.293</td><td>0.220</td><td>21.562</td><td>21.124</td></tr>
<tr><td>lame (-V0 -q7)</td><td>15.153</td><td>1.024</td><td>0.362</td><td>0.377</td><td>0.336</td><td>20.458</td><td>19.473</td></tr>
<tr><td>lame (-V1 -q2)</td><td>14.894</td><td>1.659</td><td>0.353</td><td>0.406</td><td>0.353</td><td>18.076</td><td>17.457</td></tr>
<tr><td>lame (-V1 -q7)</td><td>11.365</td><td>1.009</td><td>0.326</td><td>0.545</td><td>0.616</td><td>16.228</td><td>15.481</td></tr>
<tr><td>lame (-V2 -q2)</td><td>12.621</td><td>1.615</td><td>0.336</td><td>0.494</td><td>0.455</td><td>16.858</td><td>15.607</td></tr>
<tr><td>lame (-V2 -q7)</td><td>9.988</td><td>0.993</td><td>0.305</td><td>0.624</td><td>0.736</td><td>15.335</td><td>13.493</td></tr>
<tr><td>lame (-V3 -q2)</td><td>11.399</td><td>1.573</td><td>0.324</td><td>0.545</td><td>0.519</td><td>16.199</td><td>14.471</td></tr>
<tr><td>lame (-V3 -q7)</td><td>9.242</td><td>0.988</td><td>0.311</td><td>0.670</td><td>0.827</td><td>14.842</td><td>11.912</td></tr>
<tr><td>lame (-V4 -q2)</td><td>9.756</td><td>1.516</td><td>0.303</td><td>0.641</td><td>0.634</td><td>15.164</td><td>13.712</td></tr>
<tr><td>lame (-V4 -q7)</td><td>8.175</td><td>0.989</td><td>0.288</td><td>0.744</td><td>0.909</td><td>14.192</td><td>13.157</td></tr>
<tr><td>lame (-V5 -q2)</td><td>7.757</td><td>1.402</td><td>0.316</td><td>0.777</td><td>0.816</td><td>13.815</td><td>13.200</td></tr>
<tr><td>lame (-V5 -q7)</td><td>6.751</td><td>0.957</td><td>0.271</td><td>0.855</td><td>1.128</td><td>13.003</td><td>11.639</td></tr>
<tr><td>lame (-V6 -q2)</td><td>6.432</td><td>1.336</td><td>0.288</td><td>0.897</td><td>1.067</td><td>12.219</td><td>11.603</td></tr>
<tr><td>lame (-V6 -q7)</td><td>5.898</td><td>0.951</td><td>0.283</td><td>0.939</td><td>1.380</td><td>11.696</td><td>10.423</td></tr>
<tr><td rowspan="5">wavpack</td><td>wavpack (-b128)</td><td>14.189</td><td>0.617</td><td>0.434</td><td>0.744</td><td>0.233</td><td>21.498</td><td>21.185</td></tr>
<tr><td>wavpack (-b160)</td><td>14.189</td><td>0.609</td><td>0.432</td><td>0.744</td><td>0.233</td><td>21.498</td><td>21.185</td></tr>
<tr><td>wavpack (-b192)</td><td>14.189</td><td>0.609</td><td>0.432</td><td>0.744</td><td>0.233</td><td>21.498</td><td>21.185</td></tr>
<tr><td>wavpack (-b256)</td><td>18.753</td><td>0.717</td><td>0.530</td><td>0.291</td><td>0.107</td><td>25.404</td><td>24.152</td></tr>
<tr><td>wavpack (-b320)</td><td>23.781</td><td>0.773</td><td>0.558</td><td>0.133</td><td>0.055</td><td>28.566</td><td>28.204</td></tr>
<tr><td rowspan="12">wma(CBR)</td><td>wmaencode (-c pro -m cbr -b 128)</td><td>9.154</td><td>1.764</td><td>0.149</td><td>0.628</td><td>0.498</td><td>15.337</td><td>14.631</td></tr>
<tr><td>wmaencode (-c pro -m cbr -b 160)</td><td>11.426</td><td>1.780</td><td>0.156</td><td>0.514</td><td>0.409</td><td>16.779</td><td>15.690</td></tr>
<tr><td>wmaencode (-c pro -m cbr -b 192)</td><td>13.699</td><td>1.822</td><td>0.166</td><td>0.407</td><td>0.339</td><td>17.765</td><td>17.012</td></tr>
<tr><td>wmaencode (-c pro -m cbr -b 256)</td><td>18.243</td><td>1.967</td><td>0.183</td><td>0.286</td><td>0.257</td><td>19.654</td><td>18.757</td></tr>
<tr><td>wmaencode (-c pro -m cbr -b 384)</td><td>27.333</td><td>2.516</td><td>0.208</td><td>0.116</td><td>0.102</td><td>23.531</td><td>22.869</td></tr>
<tr><td>wmaencode (-c pro -m cbr -b 440)</td><td>31.311</td><td>2.387</td><td>0.213</td><td>0.082</td><td>0.075</td><td>25.096</td><td>24.314</td></tr>
<tr><td>wmaencode (-c pro -m cbr2pass -b 128)</td><td>9.154</td><td>4.871</td><td>0.148</td><td>0.601</td><td>0.479</td><td>15.914</td><td>15.056</td></tr>
<tr><td>wmaencode (-c pro -m cbr2pass -b 160)</td><td>11.426</td><td>5.086</td><td>0.164</td><td>0.490</td><td>0.393</td><td>17.368</td><td>16.187</td></tr>
<tr><td>wmaencode (-c pro -m cbr2pass -b 192)</td><td>13.699</td><td>5.484</td><td>0.168</td><td>0.389</td><td>0.335</td><td>18.228</td><td>16.350</td></tr>
<tr><td>wmaencode (-c pro -m cbr2pass -b 256)</td><td>18.243</td><td>6.282</td><td>0.185</td><td>0.275</td><td>0.250</td><td>19.939</td><td>19.214</td></tr>
<tr><td>wmaencode (-c pro -m cbr2pass -b 384)</td><td>27.333</td><td>7.489</td><td>0.210</td><td>0.110</td><td>0.099</td><td>23.963</td><td>22.975</td></tr>
<tr><td>wmaencode (-c pro -m cbr2pass -b 440)</td><td>31.311</td><td>7.054</td><td>0.215</td><td>0.075</td><td>0.069</td><td>25.661</td><td>24.577</td></tr>
<tr><td rowspan="12">wma(VBR)</td><td>wmaencode (-c pro -m vbr -q 10)</td><td>3.625</td><td>4.316</td><td>0.126</td><td>1.446</td><td>1.909</td><td>9.093</td><td>8.548</td></tr>
<tr><td>wmaencode (-c pro -m vbr -q 25)</td><td>5.711</td><td>2.412</td><td>0.134</td><td>0.878</td><td>0.869</td><td>14.092</td><td>13.196</td></tr>
<tr><td>wmaencode (-c pro -m vbr -q 50)</td><td>7.479</td><td>2.435</td><td>0.141</td><td>0.639</td><td>0.637</td><td>15.590</td><td>14.639</td></tr>
<tr><td>wmaencode (-c pro -m vbr -q 75)</td><td>9.265</td><td>2.493</td><td>0.151</td><td>0.545</td><td>0.595</td><td>16.158</td><td>15.559</td></tr>
<tr><td>wmaencode (-c pro -m vbr -q 90)</td><td>12.479</td><td>2.568</td><td>0.160</td><td>0.445</td><td>0.476</td><td>17.442</td><td>16.463</td></tr>
<tr><td>wmaencode (-c pro -m vbr -q 98)</td><td>19.919</td><td>2.644</td><td>0.209</td><td>0.201</td><td>0.206</td><td>21.262</td><td>19.002</td></tr>
<tr><td>wmaencode (-c pro -m vbr2pass -q 10)</td><td>9.138</td><td>4.985</td><td>0.148</td><td>0.512</td><td>0.466</td><td>16.950</td><td>15.628</td></tr>
<tr><td>wmaencode (-c pro -m vbr2pass -q 25)</td><td>9.138</td><td>5.077</td><td>0.157</td><td>0.512</td><td>0.466</td><td>16.950</td><td>15.628</td></tr>
<tr><td>wmaencode (-c pro -m vbr2pass -q 50)</td><td>9.138</td><td>5.004</td><td>0.150</td><td>0.512</td><td>0.466</td><td>16.950</td><td>15.628</td></tr>
<tr><td>wmaencode (-c pro -m vbr2pass -q 75)</td><td>9.138</td><td>4.905</td><td>0.149</td><td>0.512</td><td>0.466</td><td>16.950</td><td>15.628</td></tr>
<tr><td>wmaencode (-c pro -m vbr2pass -q 90)</td><td>9.138</td><td>4.910</td><td>0.153</td><td>0.512</td><td>0.466</td><td>16.950</td><td>15.628</td></tr>
<tr><td>wmaencode (-c pro -m vbr2pass -q 98)</td><td>9.138</td><td>4.940</td><td>0.153</td><td>0.512</td><td>0.466</td><td>16.950</td><td>15.628</td></tr>
<tr><td rowspan="5">opus</td><td>opus (--bitrate 64)</td><td>5.768</td><td>2.036</td><td>1.012</td><td>1.175</td><td>1.755</td><td>9.767</td><td>8.934</td></tr>
<tr><td>opus (--bitrate 80)</td><td>7.009</td><td>2.144</td><td>1.034</td><td>0.999</td><td>1.352</td><td>11.005</td><td>10.146</td></tr>
<tr><td>opus (--bitrate 96)</td><td>8.198</td><td>2.230</td><td>1.092</td><td>0.887</td><td>1.157</td><td>11.694</td><td>10.772</td></tr>
<tr><td>opus (--bitrate 128)</td><td>10.494</td><td>2.310</td><td>1.101</td><td>0.703</td><td>0.869</td><td>13.093</td><td>12.174</td></tr>
<tr><td>opus (--bitrate 160)</td><td>12.809</td><td>2.405</td><td>1.148</td><td>0.557</td><td>0.724</td><td>13.923</td><td>13.105</td></tr>
<tr><td rowspan="12">lossyflac</td><td>lossyflac (-q I|-1)</td><td>51.658</td><td>4.063</td><td>0.184</td><td>0.006</td><td>0.002</td><td>35.425</td><td>35.435</td></tr>
<tr><td>lossyflac (-q I|-4)</td><td>46.145</td><td>4.119</td><td>0.210</td><td>0.006</td><td>0.002</td><td>35.425</td><td>35.435</td></tr>
<tr><td>lossyflac (-q I|-7)</td><td>45.873</td><td>4.678</td><td>0.209</td><td>0.006</td><td>0.002</td><td>35.425</td><td>35.435</td></tr>
<tr><td>lossyflac (-q H|-1)</td><td>45.007</td><td>7.558</td><td>0.191</td><td>0.032</td><td>0.022</td><td>29.324</td><td>28.024</td></tr>
<tr><td>lossyflac (-q H|-4)</td><td>39.584</td><td>7.599</td><td>0.203</td><td>0.032</td><td>0.022</td><td>29.324</td><td>28.024</td></tr>
<tr><td>lossyflac (-q H|-7)</td><td>39.385</td><td>8.108</td><td>0.206</td><td>0.032</td><td>0.022</td><td>29.324</td><td>28.024</td></tr>
<tr><td>lossyflac (-q S|-1)</td><td>42.657</td><td>8.156</td><td>0.187</td><td>0.045</td><td>0.033</td><td>28.009</td><td>26.144</td></tr>
<tr><td>lossyflac (-q S|-4)</td><td>37.273</td><td>8.161</td><td>0.210</td><td>0.045</td><td>0.033</td><td>28.009</td><td>26.144</td></tr>
<tr><td>lossyflac (-q S|-7)</td><td>37.057</td><td>8.706</td><td>0.208</td><td>0.045</td><td>0.033</td><td>28.009</td><td>26.144</td></tr>
<tr><td>lossyflac (-q X|-1)</td><td>29.367</td><td>10.151</td><td>0.182</td><td>0.293</td><td>0.190</td><td>21.176</td><td>18.572</td></tr>
<tr><td>lossyflac (-q X|-4)</td><td>24.759</td><td>10.142</td><td>0.200</td><td>0.293</td><td>0.190</td><td>21.176</td><td>18.572</td></tr>
<tr><td>lossyflac (-q X|-7)</td><td>24.619</td><td>10.754</td><td>0.201</td><td>0.293</td><td>0.190</td><td>21.176</td><td>18.572</td></tr>
<tr><td rowspan="4">lossytak</td><td>lossytak (-q I|-p2m)</td><td>44.790</td><td>5.625</td><td>0.236</td><td>0.006</td><td>0.002</td><td>35.425</td><td>35.435</td></tr>
<tr><td>lossytak (-q H|-p2m)</td><td>38.254</td><td>9.139</td><td>0.234</td><td>0.032</td><td>0.022</td><td>29.324</td><td>28.024</td></tr>
<tr><td>lossytak (-q S|-p2m)</td><td>35.909</td><td>9.721</td><td>0.233</td><td>0.045</td><td>0.033</td><td>28.009</td><td>26.144</td></tr>
<tr><td>lossytak (-q X|-p2m)</td><td>22.938</td><td>11.670</td><td>0.217</td><td>0.293</td><td>0.190</td><td>21.176</td><td>18.572</td></tr>
<tr><td rowspan="12">lossywv</td><td>lossywv (-q I|-f)</td><td>51.504</td><td>4.305</td><td>0.366</td><td>0.006</td><td>0.002</td><td>35.425</td><td>35.435</td></tr>
<tr><td>lossywv (-q I|)</td><td>46.235</td><td>4.391</td><td>0.467</td><td>0.006</td><td>0.002</td><td>35.425</td><td>35.435</td></tr>
<tr><td>lossywv (-q I|-h)</td><td>45.697</td><td>4.648</td><td>0.519</td><td>0.006</td><td>0.002</td><td>35.425</td><td>35.435</td></tr>
<tr><td>lossywv (-q H|-f)</td><td>46.494</td><td>7.889</td><td>0.376</td><td>0.032</td><td>0.022</td><td>29.324</td><td>28.024</td></tr>
<tr><td>lossywv (-q H|)</td><td>41.368</td><td>8.083</td><td>0.478</td><td>0.032</td><td>0.022</td><td>29.324</td><td>28.024</td></tr>
<tr><td>lossywv (-q H|-h)</td><td>41.025</td><td>8.428</td><td>0.534</td><td>0.032</td><td>0.022</td><td>29.324</td><td>28.024</td></tr>
<tr><td>lossywv (-q S|-f)</td><td>44.313</td><td>8.529</td><td>0.376</td><td>0.045</td><td>0.033</td><td>28.009</td><td>26.144</td></tr>
<tr><td>lossywv (-q S|)</td><td>39.219</td><td>8.717</td><td>0.473</td><td>0.045</td><td>0.033</td><td>28.009</td><td>26.144</td></tr>
<tr><td>lossywv (-q S|-h)</td><td>38.912</td><td>9.116</td><td>0.539</td><td>0.045</td><td>0.033</td><td>28.009</td><td>26.144</td></tr>
<tr><td>lossywv (-q X|-f)</td><td>32.060</td><td>10.606</td><td>0.370</td><td>0.293</td><td>0.190</td><td>21.176</td><td>18.572</td></tr>
<tr><td>lossywv (-q X|)</td><td>27.377</td><td>10.866</td><td>0.473</td><td>0.293</td><td>0.190</td><td>21.176</td><td>18.572</td></tr>
<tr><td>lossywv (-q X|-h)</td><td>27.375</td><td>11.261</td><td>0.551</td><td>0.293</td><td>0.190</td><td>21.176</td><td>18.572</td></tr>
<tr><td rowspan="8">aac(VBR)</td><td>neroaac (-q 0.1)</td><td>1.682</td><td>1.320</td><td>0.637</td><td>1.778</td><td>2.609</td><td>7.335</td><td>6.495</td></tr>
<tr><td>neroaac (-q 0.3)</td><td>5.787</td><td>2.558</td><td>0.540</td><td>0.978</td><td>0.768</td><td>13.445</td><td>12.993</td></tr>
<tr><td>neroaac (-q 0.5)</td><td>11.684</td><td>2.553</td><td>0.267</td><td>0.484</td><td>0.575</td><td>15.643</td><td>14.743</td></tr>
<tr><td>neroaac (-q 0.7)</td><td>18.125</td><td>2.573</td><td>0.318</td><td>0.269</td><td>0.411</td><td>16.073</td><td>15.259</td></tr>
<tr><td>neroaac (-q 0.9)</td><td>25.978</td><td>2.747</td><td>0.355</td><td>0.186</td><td>0.390</td><td>16.504</td><td>15.670</td></tr>
<tr><td>qaac (-V 31)</td><td>5.016</td><td>1.784</td><td>0.219</td><td>1.266</td><td>1.941</td><td>8.907</td><td>7.916</td></tr>
<tr><td>qaac (-V 63)</td><td>9.560</td><td>1.902</td><td>0.264</td><td>0.683</td><td>0.776</td><td>13.421</td><td>12.543</td></tr>
<tr><td>qaac (-V 95)</td><td>14.976</td><td>1.967</td><td>0.285</td><td>0.424</td><td>0.436</td><td>15.896</td><td>14.685</td></tr>
<tr><td rowspan="10">aac(CBR)</td><td>neroaac (-cbr 128)</td><td>0.908</td><td>1.154</td><td>0.602</td><td>2.575</td><td>4.117</td><td>4.780</td><td>4.247</td></tr>
<tr><td>neroaac (-cbr 160)</td><td>0.908</td><td>1.180</td><td>0.597</td><td>2.575</td><td>4.117</td><td>4.780</td><td>4.247</td></tr>
<tr><td>neroaac (-cbr 192)</td><td>0.908</td><td>1.159</td><td>0.595</td><td>2.575</td><td>4.117</td><td>4.780</td><td>4.247</td></tr>
<tr><td>neroaac (-cbr 256)</td><td>0.908</td><td>1.159</td><td>0.596</td><td>2.575</td><td>4.117</td><td>4.780</td><td>4.247</td></tr>
<tr><td>neroaac (-cbr 320)</td><td>0.908</td><td>1.156</td><td>0.603</td><td>2.575</td><td>4.117</td><td>4.780</td><td>4.247</td></tr>
<tr><td>qaac (-c 128)</td><td>9.182</td><td>1.933</td><td>0.247</td><td>0.747</td><td>0.860</td><td>12.895</td><td>12.130</td></tr>
<tr><td>qaac (-c 160)</td><td>11.451</td><td>1.975</td><td>0.264</td><td>0.594</td><td>0.659</td><td>14.064</td><td>13.262</td></tr>
<tr><td>qaac (-c 192)</td><td>13.719</td><td>2.003</td><td>0.287</td><td>0.513</td><td>0.542</td><td>14.920</td><td>13.728</td></tr>
<tr><td>qaac (-c 256)</td><td>18.256</td><td>2.097</td><td>0.299</td><td>0.360</td><td>0.421</td><td>16.306</td><td>15.343</td></tr>
<tr><td>qaac (-c 320)</td><td>22.793</td><td>2.226</td><td>0.310</td><td>0.226</td><td>0.248</td><td>18.001</td><td>17.034</td></tr>
<tr><td rowspan="3">vorbis</td><td>oggenc (-q 2)</td><td>4.838</td><td>3.668</td><td>0.151</td><td>1.235</td><td>1.821</td><td>11.147</td><td>10.347</td></tr>
<tr><td>oggenc (-q 7)</td><td>10.788</td><td>2.865</td><td>0.165</td><td>0.477</td><td>0.682</td><td>15.244</td><td>14.480</td></tr>
<tr><td>oggenc (-q 10)</td><td>24.667</td><td>3.103</td><td>0.206</td><td>0.166</td><td>0.251</td><td>18.222</td><td>18.569</td></tr>
<tr><td rowspan="3">musepack</td><td>mpc (--standard)</td><td>11.839</td><td>2.697</td><td>0.391</td><td>0.557</td><td>0.482</td><td>16.371</td><td>15.138</td></tr>
<tr><td>mpc (--extreme)</td><td>14.679</td><td>2.716</td><td>0.416</td><td>0.454</td><td>0.341</td><td>17.961</td><td>16.623</td></tr>
<tr><td>mpc (--insane)</td><td>17.242</td><td>2.710</td><td>0.382</td><td>0.373</td><td>0.246</td><td>19.475</td><td>18.167</td></tr>
</table>