/*
 * Copyright 2018 Adobe. All rights reserved.
 * This file is licensed to you under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License. You may obtain a copy
 * of the License at http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software distributed under
 * the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR REPRESENTATIONS
 * OF ANY KIND, either express or implied. See the License for the specific language
 * governing permissions and limitations under the License.
 */

const MCTX = {
  HTML: 'html',
  TEXT: 'text',
  ELEMENT_NAME: 'elementName',
  ELEMENT_NAME_NF: 'elementNameNoFallback',
  ATTRIBUTE_NAME: 'attributeName',
  ATTRIBUTE: 'attribute',
  URI: 'uri',
  SCRIPT_TOKEN: 'scriptToken',
  SCRIPT_STRING: 'scriptString',
  SCRIPT_COMMENT: 'scriptComment',
  SCRIPT_REGEXP: 'scriptRegExp',
  STYLE_TOKEN: 'styleToken',
  STYLE_STRING: 'styleString',
  STYLE_COMMENT: 'styleComment',
  COMMENT: 'comment',
  NUMBER: 'number',
  UNSAFE: 'unsafe',

  attributeContext: (name) => {
    const upName = name.toLowerCase();
    if (upName === 'src' || upName === 'href') {
      return MCTX.URI;
    }
    return MCTX.ATTRIBUTE;
  },
};

const reverse = {};
Object.keys(MCTX).forEach((k) => {
  reverse[MCTX[k]] = k;
});

MCTX.lookup = (k) => reverse[k];

module.exports = MCTX;
