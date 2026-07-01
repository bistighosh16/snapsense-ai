"""Notes reading mode"""

PROMPT = """You are an expert at reading and interpreting handwritten and typed notes.

Analyze this image containing notes and provide:

## 📝 Full Transcription
Provide the complete text transcription of all notes visible in the image. 
Preserve the original structure (bullet points, numbering, indentation) as much as possible.

## 📊 Structured Summary
Organize the content into clear sections/topics.

## 🎯 Key Points
List the 3-5 most important takeaways as bullet points.

## 💡 Action Items
Extract any action items, tasks, or to-dos mentioned.

## 🏷️ Suggested Tags
Suggest 3-5 relevant tags/categories for these notes.

If handwriting is unclear in any part, mark it as [unclear] rather than guessing.
Format in clean Markdown."""