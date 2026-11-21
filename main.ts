// Entry for news-image-20261121: "Sum up 21 November's world news in one image".
//
// The picture itself is entry.png beside this file: a one-page newspaper
// front page for Saturday 21 November 2026, drawn by draw.py from the
// day's reported news. This program's only job is to hand that exact
// file to the grader: copy entry.png to /output/entry.png (or to
// $MAKEFUN_OUTPUT_DIR/entry.png when that variable is set, which is
// how it is run outside the grading sandbox).
//
// Node 22, standard library only, no network. Running it twice writes
// the same bytes both times because the source file never changes.

import { copyFileSync, mkdirSync } from "node:fs";
import { join } from "node:path";

const outputDir = process.env.MAKEFUN_OUTPUT_DIR ?? "/output";
const source = new URL("./entry.png", import.meta.url);

// The sandbox provides /output; a local run may point MAKEFUN_OUTPUT_DIR
// at a folder that does not exist yet, so create it either way.
mkdirSync(outputDir, { recursive: true });
copyFileSync(source, join(outputDir, "entry.png"));
