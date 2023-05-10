import torch
import torch.nn as nn



class AttentionMethod(nn.ModuleList):
    def __init__(self, hidden_dim):
        super(AttentionMethod, self).__init__()

        self.attn = nn.Linear(hidden_dim, hidden_dim)
        self.contx = nn.Linear(hidden_dim, 1, bias=False)


    def align_to_context(self, input, context, mask):
        """
        :description: align input to context
        :param input: (batch_size, input_len, input_size)
        :param context: (batch_size, context_len, context_size)
        :param mask: (batch_size, context_len)
        :param self:
        :return: (batch_size, input_len, context_size)
        """

        batch_size, input_len, input_size = input.size()
        context_len = context.size(1)

        align = torch.bmm(input, context.transpose(1, 2))

        # softmax
        align = align.view(batch_size * input_len, context_len)
        mask = mask.view(batch_size * context_len)
        align = torch.masked_fill(align, mask.unsqueeze(1).bool(), -float('inf'))
        align = torch.softmax(align, dim=1).view(batch_size, input_len, context_len)

        # weighted sum
        return torch.bmm(align, context)



    def forward(self, input, context, mask):
        """
        :param input: (batch_size, input_len, input_size)
        :param context: (batch_size, context_len, context_size)
        :param mask: (batch_size, context_len)
        :param self:
        :return: (batch_size, input_size)
        """

        context = self.align_to_context(input, context, mask)

        input = torch.cat([input, context], dim=2)

        output, _ = self.rnn(input)

        return self.attention(output, mask)




class ATTClassifier(nn.Module):
    def __init__(self, in_feature, class_num=1, dropout_prob=0.2):
        super(ATTClassifier, self).__init__()
        self.attention = AttentionMethod(in_feature)
        self.classifier = nn.Sequential(
            nn.Linear(in_feature, in_feature),
            nn.ReLU(),
            nn.Dropout(dropout_prob),
            nn.Linear(in_feature, class_num)
        )


    def forward(self, input, context, mask):
        """
        :param input: (batch_size, input_len, input_size)
        :param context: (batch_size, context_len, context_size)
        :param mask: (batch_size, context_len)
        :param self:
        :return: (batch_size, class_num)
        """
        output = self.attention(input, context, mask)
        output = self.classifier(output)

        return output
