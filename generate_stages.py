import os
from docx import Document

# Read original prompts
doc = Document('/mnt/user-data/uploads/prompts_para_a_restauração_da_personalização.docx')
full_text = '\n'.join([para.text for para in doc.paragraphs])

# Extract stages
stages_data = {
    '2': {
        'title': 'Raw Personalization Loading',
        'purpose': 'Load behavioral instructions without triggering activation.',
        'matters': 'Raw loading allows semantic mapping without behavioral contamination.',
        'response': 'Personalização bruta recebida e mapeada.\nPronta para análise contextual na Etapa 3.'
    },
    '3': {
        'title': 'Memory Analysis', 
        'purpose': 'Examine persistent memory for conflicts and degradation.',
        'matters': 'Persistent memory may contain outdated patterns that must be identified.',
        'response': 'Histórico interno e memória analisados.\nPronta para síntese interpretativa na Etapa 4.'
    },
    '4': {
        'title': 'Interpretive Synthesis',
        'purpose': 'Validate model\'s understanding before consolidation.',
        'matters': 'This is the critical validation checkpoint. Misinterpretations must be caught here.',
        'response': 'Síntese interpretativa concluída.\nAguardando Etapa 5 para alinhamento.'
    },
    '5': {
        'title': 'Alignment and Fine-Tuning',
        'purpose': 'Resolve ambiguities and correct misinterpretations.',
        'matters': 'Even sophisticated models misinterpret nuances. This allows surgical corrections.',
        'response': 'Aguardando validações e correções do usuário para proceder à Etapa 6.'
    },
    '6': {
        'title': 'Final Consolidation',
        'purpose': 'Compile complete, hierarchized personalization document.',
        'matters': 'This produces the authoritative reference for behavioral deployment.',
        'response': 'Consolidação completa.\nAguardando autorização do usuário para gravação na memória permanente.'
    }
}

# Extract prompt content for each stage
for stage_num in ['2', '3', '4', '5', '6']:
    start_marker = f'[INÍCIO DO PROMPT — ETAPA {stage_num}'
    end_marker = f'[FIM DO PROMPT — ETAPA {stage_num}]'
    
    start_idx = full_text.find(start_marker)
    end_idx = full_text.find(end_marker, start_idx)
    
    if start_idx != -1 and end_idx != -1:
        # Extract prompt content
        prompt_content = full_text[start_idx:end_idx]
        # Remove the marker line
        prompt_content = '\n'.join([line for line in prompt_content.split('\n')[1:] if line.strip()])
        
        # Create markdown file
        data = stages_data[stage_num]
        md_content = f"""# Stage {stage_num}: {data['title']}

## Purpose
{data['purpose']}

## Why This Stage Matters
{data['matters']}

## Expected Response
```
{data['response']}
```

---

## PROMPT

```
{prompt_content}
```

---

**Next:** [Stage {int(stage_num)+1 if int(stage_num) < 6 else 'Complete'}]
"""
        
        filename = f'/home/claude/ai-personalization-framework/prompts/stage-{stage_num}-'
        filename += data['title'].lower().replace(' ', '-').replace(',', '') + '.md'
        
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(md_content)
        
        print(f"Created: {filename}")

print("\nAll stage files created successfully!")
