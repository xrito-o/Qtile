const char *colorname[] = {

  /* 8 normal colors */
  [0] = "#1b1e25", /* black   */
  [1] = "#667475", /* red     */
  [2] = "#947D74", /* green   */
  [3] = "#74857A", /* yellow  */
  [4] = "#617686", /* blue    */
  [5] = "#738B8B", /* magenta */
  [6] = "#7697A5", /* cyan    */
  [7] = "#c6c6c8", /* white   */

  /* 8 bright colors */
  [8]  = "#626878",  /* black   */
  [9]  = "#667475",  /* red     */
  [10] = "#947D74", /* green   */
  [11] = "#74857A", /* yellow  */
  [12] = "#617686", /* blue    */
  [13] = "#738B8B", /* magenta */
  [14] = "#7697A5", /* cyan    */
  [15] = "#c6c6c8", /* white   */

  /* special colors */
  [256] = "#1b1e25", /* background */
  [257] = "#c6c6c8", /* foreground */
  [258] = "#c6c6c8",     /* cursor */
};

/* Default colors (colorname index)
 * foreground, background, cursor */
 unsigned int defaultbg = 0;
 unsigned int defaultfg = 257;
 unsigned int defaultcs = 258;
 unsigned int defaultrcs= 258;
