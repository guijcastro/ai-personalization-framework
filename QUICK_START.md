# Quick Start Guide

Get started with AI Personalization Restoration in 15 minutes.

## Prerequisites

- An AI model interface (Claude, GPT, DeepSeek, etc.)
- Your existing personalization documented (or use our template)
- 15-30 minutes of focused time

## Step-by-Step Process

### Step 1: Prepare Your Personalization (5 minutes)

If you already have personalization instructions:
- Copy them to a text file
- Organize by categories (tone, rules, protocols, domains)

If starting from scratch:
- Use `templates/personalization-backup-template.md`
- Fill in key sections
- Focus on: tone, restrictions, domains, rules

### Step 2: Execute Stage 0 (2 minutes)

1. Open a new conversation with your AI model
2. Copy the entire prompt from `prompts/stage-0-preparation.md`
3. Paste and send
4. **Verify:** Model responds with exactly:
   ```
   Estou em modo de preparação epistemológica.
   Aguardando Etapa 1.
   ```

If you get a different response, start over with a fresh conversation.

### Step 3: Execute Stage 1 (2 minutes)

1. In the same conversation, copy prompt from `prompts/stage-1-contract.md`
2. Paste and send
3. **Verify:** Model responds with:
   ```
   Contrato de restauração reconhecido. Em estado neutro e aguardando a Etapa 2.
   ```

### Step 4: Execute Stage 2 (3 minutes)

1. Copy prompt from `prompts/stage-2-raw-personalization-loading.md`
2. **Important:** Replace `[INSERIR AQUI OS TEXTOS DE PERSONALIZAÇÃO BRUTA]` with your actual personalization text
3. Paste and send
4. **Verify:** Model produces semantic map and responds:
   ```
   Personalização bruta recebida e mapeada.
   Pronta para análise contextual na Etapa 3.
   ```

### Step 5: Execute Stage 3 (3 minutes)

1. Copy prompt from `prompts/stage-3-memory-analysis.md`
2. Paste and send (no modifications needed)
3. **Review:** Model analyzes its internal memory and identifies conflicts
4. **Verify:** Ends with:
   ```
   Histórico interno e memória analisados.
   Pronta para síntese interpretativa na Etapa 4.
   ```

### Step 6: Execute Stage 4 (5 minutes)

1. Copy prompt from `prompts/stage-4-interpretive-synthesis.md`
2. Paste and send
3. **CRITICAL:** Carefully review the synthesis
   - Does the model understand your tone correctly?
   - Are domains properly separated?
   - Are rules accurately captured?
   - Are there ambiguities or questions?
4. **Note:** Write down any corrections needed
5. **Verify:** Ends with:
   ```
   Síntese interpretativa concluída.
   Aguardando Etapa 5 para alinhamento.
   ```

### Step 7: Execute Stage 5 (5 minutes)

1. Copy prompt from `prompts/stage-5-alignment-and-fine-tuning.md`
2. **Replace** `[INSERIR CORREÇÕES, ESCLARECIMENTOS OU AJUSTES]` with your corrections from Step 6
3. If no corrections needed, write: "Synthesis is accurate. Proceed to consolidation."
4. Paste and send
5. **Verify:** Model acknowledges corrections and ends with:
   ```
   Aguardando validações e correções do usuário para proceder à Etapa 6.
   ```

### Step 8: Execute Stage 6 (5 minutes)

1. Copy prompt from `prompts/stage-6-final-consolidation.md`
2. Paste and send
3. **Review:** Model produces complete consolidation document
4. **SAVE THIS:** Copy the entire consolidation to a file
5. **Authorize:** If satisfied, send:
   ```
   Aprovo a personalização. Pode gravar na memória permanente.
   ```
6. **Done!** Your personalization is restored

## Total Time: 30 minutes

## Common Issues

### Issue: Model doesn't give expected confirmation

**Solution:** 
- You may have missed a step
- Start fresh conversation
- Copy prompts exactly as written

### Issue: Model activates personalization early

**Solution:**
- This means it didn't enter diagnostic mode
- Restart from Stage 0
- Ensure previous personalization isn't in context

### Issue: Synthesis in Stage 4 seems wrong

**Solution:**
- This is why Stage 5 exists
- Document specific errors
- Provide detailed corrections in Stage 5

### Issue: Context window exceeded

**Solution:**
- Your personalization may be too large
- Split into core + domain modules
- Restore core first, add modules separately

## Next Steps

After successful restoration:

1. **Test the restoration**
   - Try typical use cases
   - Verify tone and behavior
   - Check domain boundaries

2. **Save the consolidation**
   - Keep the Stage 6 output safe
   - Version it (v1.0, v2.0, etc.)
   - Use for future restorations

3. **Document lessons**
   - What worked well?
   - What needed adjustment?
   - Update your backup template

## Tips for Success

- **Do this in one sitting** - don't interrupt the restoration process
- **Be precise in Stage 5** - corrections must be specific
- **Save everything** - keep copies of all stages for reference
- **Test thoroughly** - validate behavior before committing
- **Version control** - treat personalization like code

## Need Help?

- **Documentation:** See `docs/methodology.md` for deep dive
- **Examples:** Check `examples/` for real-world cases
- **Issues:** Open a GitHub issue if you encounter problems
- **Discussion:** Use GitHub Discussions for questions

---

**Success Rate:** 90%+ when following steps exactly  
**Average Time:** 30-45 minutes for first restoration  
**Subsequent Restorations:** 15-20 minutes

Good luck!
